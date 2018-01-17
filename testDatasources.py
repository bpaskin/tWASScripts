################################################
# testDatasources.py                           #
# Script to test all the datasources within a  #
# WebSphere cell.                              #
#                                              #
# usage:                                       #
# <profile_home>/bin/wsadmin.sh -f             #
#                  /path/to/testDatasources.py #
#                                              #
# Brian S Paskin (IBM SWG)                     #
# 13 May 2013                                  #
################################################

# Get a list of the Datasources defined in the cell
datasources = AdminConfig.list('DataSource').splitlines()

# Loop through the datasources and test ignoring
# the default ones defined by WAS
for datasource in datasources:
	# get the name of the datasource
	name = AdminConfig.showAttribute(datasource, 'name')
	
	# check the name to see if it is a WAS default and
	# test Datasource
	if ( name != "DefaultEJBTimerDataSource" ):
		try:
			AdminControl.testConnection(datasource)
			print "Testing " + name + " successful "
		except:
			print "Testing " + name + " failed " 
