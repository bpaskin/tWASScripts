# Change userid/pw for tWAS standalone LDAP
# usage: changeLDAPUseridPw.py userid env1:pw,env2:pw,env3:pw...
#
# Password should not be encrypted
#
# This examines that Bind DN from LDAP and compares it to the environment entries
# sent on the command line.
# If the environment is found then the userid is check to see if it is the same
# if it is different then the userid/pw are updated for that environment
# The soap.client.props file is updated in either case since it is possible
# that the changes arose from the DMGR
# Finally save everything off and sync nodes.

import sys, os

# make sure 2 arguments are passed
if len(sys.argv) != 2:
	print "usage: changeLDAPUseridPw.py userid env1:pw,env2:pw,env3:pw..."
  	sys.exit(1)

# get the userid passed into the script
newUserId = sys.argv[0]
envs = sys.argv[1].split(',')

# get the Standalone user registry
registry = AdminConfig.list('LDAPUserRegistry')
bindDN = AdminConfig.showAttribute(registry, 'bindDN')

for env in envs:
	envInfo = env.split(':')
	if bindDN.find(envInfo[0]) > -1:
		# Parse the env and password
		envName =  envInfo[0]
		envPw =  envInfo[1]
		print "found env " + envName

		# parse the older userid and bind domain from the current settings
		bindSplit = bindDN.split('@')
		oldUserId = bindSplit[0]
		bindDomain =  bindSplit[1]

		# check if the user already exists
		if bindDN.find(newUserId) == -1:

			# update the LDAP registry with the new userid and password
			AdminTask.configureAdminLDAPUserRegistry('[-bindDN ' + newUserId + '@' + bindDomain + ' -bindPassword ' + envPw + ']')

			# Save the configuration
			AdminConfig.save()
		else:
			print "User already exists in repository, skipping updating settings in WebSphere"

		# update soap.client.props file with the new userid and password
		# get the current directory path
		curdir = os.getcwd()
		print curdir

		# open the file for read
		file = open(curdir + '/../properties/soap.client.props', 'r')
		data = file.readlines()
		file.close()	

		# loop through the file and update the necessary lines
		for x in range(len(data)):
			if data[x].find('com.ibm.SOAP.loginUserid') > -1:
				data[x] = 'com.ibm.SOAP.loginUserid=' + newUserId + "\n"
			if data[x].find('com.ibm.SOAP.loginPassword') > -1:
				data[x] = 'com.ibm.SOAP.loginPassword=' + envPw + "\n"

		# write the data back to the file
		file = open(curdir + '/../properties/soap.client.props', 'w')
		file.writelines(data)
		file.close()
		
		print "soap.client.props file has been successfully updated"

		# exit the loop
		break

print "Userid and password changed successful"

# Sync Nodes
try:
	nodes = AdminConfig.list('Node').splitlines()
	for node in nodes:
		  nodeName = AdminConfig.showAttribute(node, 'name')
		  syncNode = AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=' + nodeName + ',*')
		  if len(syncNode) > 0:
			 AdminControl.invoke(syncNode, 'sync')
except: 
	print "Failed to sync nodes, but otherwise successfull"

# Finished
sys.exit(0)

