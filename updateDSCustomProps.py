datasources = AdminConfig.list('DataSource').splitlines()
  
for datasource in datasources:
        dsName = AdminConfig.showAttribute(datasource,'name')
        print "Datasource: " + dsName

        propertySet = AdminConfig.showAttribute(datasource,'propertySet')

        sslName = ['name', 'sslConnection']
        sslValue = ['value', 'true']
        sslAttrs = [sslName, sslValue]

        AdminConfig.create('J2EEResourceProperty', propertySet, sslAttrs)

AdminConfig.save()