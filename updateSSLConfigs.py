# Script to set All SSL Configurations to TLSv1.2
# and create a new SSL Configuration for MS AD server
# at TLSv1 and set the LDAP configuration accordingly
# 
# Tested under WASv855x
#
# Brian S Paskin (IBM R&D)
# 11 December 2015

# retrieve Cell and name
cell = AdminConfig.list('Cell')
cellName = AdminConfig.showAttribute(cell, 'name')

# retrieve all current SSL Configurations
sslConfigs = AdminTask.listSSLConfigs('[-all true -displayObjectName true ]').splitlines()

# update all current SSL Configuration to use TLSv1.2
for sslConfig in sslConfigs:
	aliasName = AdminConfig.showAttribute(sslConfig, 'alias')
	AdminTask.modifySSLConfig('[-alias ' + aliasName + ' -sslProtocol TLSv1.2]')
	
# Add new SSL Configuration for Microsoft AD
AdminTask.createSSLConfig('[-alias ADSSL -type JSSE -keyStoreName CellDefaultKeyStore -trustStoreName CellDefaultTrustStore -sslProtocol TLSv1]')

# Make the LDAP connection use the new SSL Configuration
AdminTask.configureAdminLDAPUserRegistry('[-sslEnabled true -sslConfig ADSSL]')

# Save everything
AdminConfig.save()