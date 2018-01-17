# Update all listener ports to change them to a default
# stop state.
#
# Brian S Paskin
# 28/01/2014

lports = AdminConfig.list('ListenerPort').splitlines()

for lport in lports:
	state = AdminConfig.showAttribute(lport,'stateManagement')
	AdminConfig.modify(state, '[[initialState "STOP"]]')
	
AdminConfig.save()
	