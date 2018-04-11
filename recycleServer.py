import sys

#
# Simple restart of App Server based on server name
# The app server is terminated first then restarted.
#
# Brian S Paskin
# 5 April 2018
#

def getNodeName(serverName):
	nodes = AdminConfig.list('Node').splitlines()
	for node in nodes:
		servers = AdminConfig.list('Server', node).splitlines()
		for server in servers:
			name = AdminConfig.showAttribute(server, 'name')
			if serverName == name:
				nodeName = AdminConfig.showAttribute(node, 'name')
				return nodeName
		
if ( len(sys.argv) != 1 ) :
	sys.exit( "\nusgage: restartAppServer nameOfServer\n")

serverName = sys.argv[0]

servers = AdminConfig.getid('/Server:' + serverName + '/').splitlines()

if ( len(servers) == 0) :
	sys.exit( "\nServer not found: " + serverName + "\n")
	
if ( len(servers) > 1) :
	sys.exit( "\nMore than one server with the same name found: " + serverName + "\n")
	
nodeName = getNodeName(serverName)
nodeAgent = AdminControl.completeObjectName('type=NodeAgent,node=' + nodeName + ',*')
print "Terminating server " + serverName + " on Node" + nodeName
AdminControl.invoke(nodeAgent, 'terminate', serverName)
print "Starting server " + serverName + " on Node" + nodeName
print  AdminControl.startServer(serverName, nodeName)
print "Restart Complete"

