import sys
import os

import shutil

SCRIPTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))  
print SCRIPTDIR

os.chdir(SCRIPTDIR)
a=os.listdir(SCRIPTDIR)
#print a

for item in a:
    #print a
    os.chdir(SCRIPTDIR)
    #shutil.copy(SCRIPTDIR  +  "\\Config.ini",os.path.join(SCRIPTDIR,item))
    #shutil.copy(os.path.join(SCRIPTDIR,"Config.ini"),os.path.join(SCRIPTDIR,item))
    #print os.path.join(SCRIPTDIR,"Config.ini")
    source = os.path.join(SCRIPTDIR,"Config.ini")
    destination = os.path.join(SCRIPTDIR,item)
    #print os.path.join(SCRIPTDIR,item)
    if not (source==destination):
        print "source " + source
        print "destination " + destination
        if os.path.isdir(destination):
            shutil.copy(source,destination)
   
    





            

		
		
    
