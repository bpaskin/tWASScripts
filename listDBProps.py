datasources = AdminConfig.list('Datasource').splitlines()

for datasource in datasources:
        dsName = AdminConfig.showAttribute(datasource,'name')
        print "Datasource: " + dsName
        
        propertySet = AdminConfig.showAttribute(datasource,'propertySet')
        propertyList = AdminConfig.list('J2EEResourceProperty', propertySet).splitlines()
        
        for property in propertyList:
                propName = AdminConfig.showAttribute(property, 'name')
                propValue = AdminConfig.showAttribute(property, 'value')
                print propName + " : " + propValue
