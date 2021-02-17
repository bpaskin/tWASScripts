# Traditional WebSphere Application Server scripts
Jython and other scripts for Traditional WebSphere Application Server

# changeRetryInterval.py
Change the retry interval in all web servers 

# changeStateListenerPorts.py
Change all Listener Ports to be stopped when the App Server starts up

# endpointURLs.py 
List all endpoints

# listDBProps.py
List all database properties for all databases

# showMaxThreads2.py
Show max web container threads for each App Server

# testDatasources.py 
Test all datasources

# updateJVMGenArgs.py
Add arguments to the Generic JVM Argument line

# updateSSLConfigs.py
Change the SSL Configurations to TLS v1.2 or whatever you wish

# changeRuntimeTrace.py
Allows to change the runtime trace of a server (file name, max size, number of files max, and trace format)

# PTTwithTLSv2.md
How to use the Performance Testing Toolkit with TLSv1.2

# setSecurityProperty.py
Sets a custom property under global security

# addAndConfigAppServers.py
Adds x number of App Servers to a Node, configures the JVM options and custom properties, environmental entries, custom service, HTTP and HTTPS port numbers, and Web Container thread pool

# updateDSCustomProps.py #
Update all datasources with a custom property.

# changeLDAPUseridPw.py
This will change the userid and password for a standalone LDAP given different environments.  Once changed, the soap.client.props are also updated to refelct the new userid and password.

# UpdateSDKandJVMProp
Shell and Jython script.  Finds tWAS instance and updates the profiles and servers to use the Java 1.8 Bundled with tWAS and then goes into each profile with wsadmin and adds a JVM customer property, if not already there.
