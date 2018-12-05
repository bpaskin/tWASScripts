AdminTask.setAdminActiveSecuritySettings('[-customProperties["com.ibm.ws.security.web.logoutOnHTTPSessionExpire=true"]]')
AdminConfig.save()
print "Security property set"

nodes = AdminConfig.list('Node').splitlines()
for node in nodes:
    nodeName = AdminConfig.showAttribute(node, 'name')
    nodeagent = AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=' + nodeName + ',*')
    if (len(nodeagent) > 0):
        result = AdminControl.invoke(nodeagent, 'sync')

        if (result == "true"):
            print nodeName + " synchronized"
        else:
            print nodeName + " not synchronzied correctly"