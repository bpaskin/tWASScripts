print "Creation of the environment has begun\n" 

### Variables that can be changed ####
createNodeName = 'nodeToDeployName'
createServerNames = ['ServerName1','ServerName2','ServerName3']
startingHttpPort = 9080
startingHttpsPort = 9443
conf = 1
env = 'PROD'

# Loop through the list of servers and create a new one
for createServerName in createServerNames:

	# create App Server
	server = AdminTask.createApplicationServer(createNodeName, '[-name ' + createServerName + ' -templateName default -genUniquePorts true ]')

	# Add JVM properties
	AdminTask.setJVMProperties('[-serverName ' +  createServerName + ' -nodeName  ' + createNodeName + ' -classpath [/opt/IBM/odwek/V9.0/api/ODApi.jar /opt/apps/ODWS/afp2pdf/java_api/afp2pdf.jar /opt/apps/ODWS/Line2pdf/line2pdf.jar] -verboseModeClass false -verboseModeGarbageCollection false -verboseModeJNI false -initialHeapSize 2560 -maximumHeapSize 2560 -runHProf false -hprofArguments  -debugMode false -debugArgs "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7777" -genericJvmArguments "-Dcom.sun.jndi.ldap.connect.pool.timeout=300000 -Xgcpolicy:gencon -Xmn1024m -javaagent:/usr/WebSphere/AppServer/wily/AgentNoRedefNoRetrans.jar -Dcom.wily.introscope.agentProfile=/usr/WebSphere/AppServer/wily/core/config/IntroscopeAgent.websphere.NoRedef.profile -Dcom.wily.autoprobe.logSizeInKB=10000 -Xshareclasses:none" -executableJarFileName  -disableJIT false]')

	# Add the JVM custom properties
	jvm = AdminConfig.list('JavaVirtualMachine', server)
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "AFP2PDF_INSTALL_DIR"] [description ""] [value "/opt/apps/ODWS/afp2pdf"] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "CONFIG_PATH"] [description ""] [value "/opt/apps/ECM/Config_0' + str(conf) + '/"] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "LINE2PDF_INSTALL_DIR"] [description ""] [value "/opt/apps/ODWS/Line2pdf"] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "ODGetContentServlet_URL"] [description ""] [value "https://localhost:' + str(startingHttpsPort) + '/ODWS/ODConnectorServlet"] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "current.env"] [description ""] [value ' + env +'] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "log4j.configuration"] [description ""] [value "file:///opt/apps/ECM/Config_0' + str(conf) + '/log4j.properties"] [required "false"]]')
	AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "user.dir"] [description ""] [value "/opt/apps/ODWS/Line2pdf"] [required "false"]]')

	# Add environment varianles
	env = AdminConfig.list('JavaProcessDef', server)
	AdminConfig.create('Property', env, '[[validationExpression ""] [name "IBM_HEAPDUMPDIR"] [description ""] [value "/wsapps/cores/' + createServerName +'"] [required "false"]]')
	AdminConfig.create('Property', env, '[[validationExpression ""] [name "IBM_JAVACOREDIR"] [description ""] [value "/wsapps/cores/' + createServerName +'"] [required "false"]]')
	AdminConfig.create('Property', env, '[[validationExpression ""] [name "JAVA_DUMP_OPTS"] [description ""] [value "ONANYSIGNAL(JAVADUMP[5],HEAPDUMP[5])"] [required "false"]]')
	AdminConfig.create('Property', env, '[[validationExpression ""] [name "LIBPATH"] [description ""] [value "/opt/IBM/odwek/V9.0:/opt/apps/ODWS/afp2pdf:/opt/apps/ODWS/afp2pdf/java_api:/opt/apps/ODWS/afp2pdf/locale:/opt/apps/ODWS/afp2pdf/font:/opt/apps/ODWS/Line2pdf"] [required "false"]]')
	AdminConfig.create('Property', env, '[[validationExpression ""] [name "TMPDIR"] [description ""] [value "/tmp"] [required "false"]]')

	# Update the default HTTP and HTTPS ports
	AdminTask.modifyServerPort(createServerName, '[-nodeName ' + createNodeName + ' -endPointName WC_defaulthost -host * -port ' + str(startingHttpPort) + ' -modifyShared true]')
	AdminTask.modifyServerPort(createServerName, '[-nodeName ' + createNodeName + ' -endPointName WC_defaulthost_secure -host * -port ' + str(startingHttpsPort) + ' -modifyShared true]')

	# Create a custom service for Introscope
	AdminConfig.create('CustomService', server, '[[displayName "Introscope Custom Service"] [classpath "/usr/WebSphere/AppServer/wily/common/WebAppSupport.jar"] [enable "true"] [externalConfigURL "/usr/WebSphere/AppServer/wily/common/jmxconfig.properties"] [description ""] [classname "com.wily.introscope.api.websphere.IntroscopeCustomService"]]')

	# Update the web container thread pool
	tps = AdminConfig.list('ThreadPool', server).splitlines()
	for tp in tps:
   		tpName = AdminConfig.showAttribute(tp, "name")
   		if (tpName == "WebContainer"):
			AdminConfig.modify(tp, '[[maximumSize "20"] [name "WebContainer"] [inactivityTimeout "60000"] [minimumSize "20"] [description ""] [isGrowable "false"]]')

	startingHttpPort += 1
	startingHttpsPort += 1
	conf += 1

AdminConfig.save()
