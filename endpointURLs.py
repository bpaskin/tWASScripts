import socket

hostname = socket.gethostname()

applications = AdminApp.list().splitlines()

for application in applications:
	print application
	modules = AdminApp.listModules(application).splitlines()
	
	for module in modules:
		start = module.find("#")
		end = module.find("+")
		moduleName = module[start+1:end]
		print "\t" + moduleName
		
		endPointManagers = AdminControl.queryNames("WebSphere:*,type=EndpointManager,ModuleName=" + moduleName).splitlines()

		for endPointManager in endPointManagers:
			serviceNames = AdminControl.invoke(endPointManager, "getServiceNames").splitlines()
			
			for serviceName in serviceNames:
				endpointNames = AdminControl.invoke(endPointManager, "getEndpointNames", [serviceName]).splitlines()
				
				for endpointName in endpointNames:
					print "\t\t" +  AdminControl.invoke(endPointManager, "getEndpointPartialURL", [serviceName, endpointName])
					