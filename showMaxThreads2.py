# prints the max web container threads for each app server
# Brian S Paskin (IBM SSW Boston)
# 14/02/2012

servers = AdminConfig.list('Server').splitlines()
for server in servers:
	if ( AdminConfig.showAttribute(server, 'serverType') == 'APPLICATION_SERVER' ):
		name = AdminConfig.showAttribute(server, 'name')
		tps = AdminConfig.list('ThreadPool', server).splitlines()
		for tp in tps:
			tpName = AdminConfig.showAttribute(tp, 'name')
			if (tpName == 'WebContainer'):
				threads = AdminConfig.showAttribute(tp, 'maximumSize')
				print name + " max threads = " + threads
				