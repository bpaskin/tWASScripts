# updating runtime trace within tWAS within command scripting interface
# using JMX to invoke the necessary method on the TraceService MBean
# Brian S Paskin (IBM R&D Support)
# 14/02/2018

import javax.management as mgmt 

# replace SERVER_NAME with the target server
objNameString = AdminControl.completeObjectName('WebSphere:type=TraceService,process=SERVER_NAME,*') 
objName =  mgmt.ObjectName(objNameString) 

# parameters are trace file name, maximum file size, maximum number of file, trace format
# change where necessary
# trace format must be 'basic', 'advanced', or 'loganalyzer'
parms = ['trace.log', 20, 25, 'BASIC'] 
signature = ['java.lang.String', 'int', 'int', 'java.lang.String'] 
AdminControl.invoke_jmx(objName, 'setTraceOutputToFile', parms, signature)

# check that change has been made
print AdminControl.getAttribute(objNameString, 'traceRuntimeConfig')

