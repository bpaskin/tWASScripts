jvms = AdminConfig.list('JavaVirtualMachine').splitlines()
for jvm in jvms:
	props = AdminConfig.list('Property', jvm).splitlines()

        found = 0
	for prop in props:
	   name = AdminConfig.showAttribute(prop,'name')
	   if ( name == 'com.sun.jndi.ldap.object.disableEndpointIdentification' ):
              found = 1

        if ( found == 0 ):
           AdminConfig.create('Property', jvm, '[[name com.sun.jndi.ldap.object.disableEndpointIdentification] [value true]]')

AdminConfig.save()

