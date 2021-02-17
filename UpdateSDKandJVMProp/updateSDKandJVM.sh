washomes="/usr/WebSphere/WAS8.5/AppServer85 /usr/WebSphere/AppServer /usr/WebSphere/AppServer85 /usr/WebSphere/AppServer90 /usr/WebSphere/AppServer70 /usr/WebSphere70/AppServer /usr/WebSphere80/AppServer /usr/WebSphere85/AppServer /usr/WebSphere855/AppServer /usr/WebSphere9/AppServer /usr/WebSphere90/AppServer"

# loop through list to see which are where tWAS is installed
for washome in $washomes; do

   # check to see if the directory exists
   if [ -f $washome/bin/managesdk.sh ]; then
       $washome/bin/managesdk.sh  -enableProfileAll -sdkName 1.8_64_bundled -enableServers
   fi

   # get the profiles
   if [ -d $washome/profiles ]; then
      profiles=`ls -d $washome/profiles/*`

      for profile in $profiles; do
         $profile/bin/wsadmin.sh -f updateJVMProp.py 
      done      
   fi

done

