# #################################### #
# Jython Script to change the retry    # 
# interval for the plugin              #
#                                      #
# Brian S Paskin (IBM SSW Boston)      #   
#                                      #
# #################################### #

servers = AdminConfig.list('WebServer').splitlines()

for server in servers:
	name = AdminConfig.showAttribute(server, 'name')
	print "Changing : " + name
	plugin = AdminConfig.list('PluginServerClusterProperties', server)
	AdminConfig.modify(plugin, '[[RetryInterval 60]]')
	
AdminConfig.save()