# Update all App Servers with generic JVM Property
# Brian S Paskin (IBM Boston)
# 06 January 2017

# Add this to the generic jvm args
ADDITION = " -Xnocompressedrefs"

servers = AdminTask.listServers('[-serverType APPLICATION_SERVER]').splitlines()
for server in servers:
	name = AdminConfig.showAttribute(server, 'name')
	jvm = AdminConfig.list('JavaVirtualMachine', server)
	gja = AdminConfig.showAttribute(jvm, 'genericJvmArguments')
	print name + " : " + gja 
	
	AdminConfig.modify(jvm,[['genericJvmArguments', gja + ADDITION]])
	gja = AdminConfig.showAttribute(jvm, 'genericJvmArguments')
	print name + " : " + gja 
	
AdminConfig.save()
