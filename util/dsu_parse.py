import os
import re,pdb
from xml.dom.minidom import parse, Document
op = """ dsu --config=dsuconfig.xml --remote --dsu-lin64-installer-location=Systems-Management_Application_FT56W_LN64_1.6.0_A00.BIN -p -n
DELL EMC System Update 1.6.0
Copyright (C) 2014 DELL EMC Proprietary.
Parsing configuration file...
Initiating connections...

Number of systems completed: 0/2 1% ##
Number of systems completed: 0/2 2% ###
Number of systems completed: 0/2 3% ####
Number of systems completed: 0/2 4% #####
Number of systems completed: 0/2 5% ######
Number of systems completed: 0/2 6% #######
Number of systems completed: 0/2 7% ########
Number of systems completed: 0/2 8% #########
Number of systems completed: 0/2 9% ##########
Number of systems completed: 0/2 10% ###########
Number of systems completed: 0/2 11% ############
Number of systems completed: 0/2 12% #############
Number of systems completed: 0/2 13% ##############
Number of systems completed: 0/2 14% ###############
Number of systems completed: 0/2 15% ################
Number of systems completed: 0/2 16% #################
Number of systems completed: 0/2 17% ##################
Number of systems completed: 0/2 18% ###################
Number of systems completed: 0/2 19% ####################
Number of systems completed: 0/2 20% #####################
Number of systems completed: 0/2 21% ######################
Number of systems completed: 0/2 22% #######################
Number of systems completed: 0/2 23% ########################
Number of systems completed: 0/2 24% #########################
Number of systems completed: 0/2 25% ##########################
Number of systems completed: 0/2 26% ###########################
Number of systems completed: 0/2 27% ############################
Number of systems completed: 0/2 28% #############################
Number of systems completed: 0/2 29% ##############################
Number of systems completed: 0/2 30% ###############################
Number of systems completed: 0/2 31% ################################
Number of systems completed: 0/2 32% ################################
Number of systems completed: 0/2 33% ################################
Number of systems completed: 0/2 34% ################################
Number of systems completed: 0/2 35% ################################
Number of systems completed: 0/2 36% ################################
Number of systems completed: 0/2 37% ################################
Number of systems completed: 0/2 38% ################################
Number of systems completed: 0/2 39% ################################
Number of systems completed: 0/2 40% ################################
Number of systems completed: 0/2 41% ################################
Number of systems completed: 0/2 42% ################################
Number of systems completed: 0/2 43% ################################
Number of systems completed: 0/2 44% ################################
Number of systems completed: 0/2 45% ################################
Number of systems completed: 0/2 46% ################################
Number of systems completed: 0/2 47% ################################
Number of systems completed: 0/2 48% ################################
Number of systems completed: 0/2 49% ################################
Number of systems completed: 0/2 50% ################################
Number of systems completed: 0/2 51% ################################/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/
Number of systems completed: 1/2 50% ################################
Number of systems completed: 1/2 51% ################################
Number of systems completed: 1/2 52% ################################
Number of systems completed: 1/2 53% ################################
Number of systems completed: 1/2 54% ################################
Number of systems completed: 1/2 55% ################################
Number of systems completed: 1/2 56% ################################
Number of systems completed: 1/2 57% ################################
Number of systems completed: 1/2 58% ################################
Number of systems completed: 1/2 59% ################################
Number of systems completed: 1/2 60% ################################
Number of systems completed: 1/2 61% ################################
Number of systems completed: 1/2 62% ################################
Number of systems completed: 1/2 63% ################################
Number of systems completed: 1/2 64% ################################
Number of systems completed: 1/2 65% ################################
Number of systems completed: 1/2 66% ################################
Number of systems completed: 1/2 67% ################################
Number of systems completed: 1/2 68% ################################
Number of systems completed: 1/2 69% ################################
Number of systems completed: 1/2 70% ################################
Number of systems completed: 1/2 71% ################################
Number of systems completed: 1/2 72% ################################
Number of systems completed: 1/2 73% ################################
Number of systems completed: 1/2 74% ################################
Number of systems completed: 2/2 100% ############################################################

IP:100.100.244.189 Status
DELL EMC System Update 1.6.0
Copyright (C) 2014 DELL EMC Proprietary.
Verifying catalog installation ...
Installing catalog from repository ...
Fetching dsucatalog ...
Reading the catalog ...
Fetching invcol_19J46_LN64_18_06_000_216_A00 ...
Verifying inventory collector installation ...
Getting System Inventory ...
Determining Applicable Updates ...
------------------ Update Preview -----------------
# : Type : Component : Version : Filename
---------------------------------------------------
1 : Firmware : Intel(R) Ethernet Converged Network Adapter XL710-Q2 : 18.5.17 : Network_Firmware_T6VN9_LN_18.5.17_A00
2 : BIOS : BIOS : 2.8.0 : BIOS_GC4J0_LN_2.8.0
3 : Firmware : NetXtreme BCM5720 Gigabit Ethernet PCIe (em2) : 20.8.4 : Network_Firmware_R4HKW_LN_20.8.4
4 : Firmware : PERC H330 Adapter Controller 0 Firmware : 25.5.5.0005 : SAS-RAID_Firmware_76W42_LN_25.5.5.0005_A11

Exiting DSU!

DSU exited with ReturnCode=0

IP:100.100.40.245 Status
DELL EMC System Update 1.6.0
Copyright (C) 2014 DELL EMC Proprietary.
Verifying catalog installation ...
Installing catalog from repository ...
Fetching dsucatalog ...
Reading the catalog ...
Fetching invcol_19J46_LN64_18_06_000_216_A00 ...
Verifying inventory collector installation ...
Getting System Inventory ...
Determining Applicable Updates ...
------------------ Update Preview -----------------
# : Type : Component : Version : Filename
---------------------------------------------------
1 : BIOS : BIOS : 1.8.0 : BIOS_3F75P_LN_1.8.0

Exiting DSU!

DSU exited with ReturnCode=0

NOTE: The preview option displays the components which can be updated based on Catalog. This option does not update.
Run --inventory for checking the component status post DSU commit.
Exiting DSU!

"""

#pdb.set_trace()
def parse_xml(catalog):
        dom = parse(catalog)
        return dom
ips = [] 
del_log = 'del /Q *.txt'
os.system(del_log)
package_xml = "dsuconfig.xml"
for package_node in parse_xml(package_xml).getElementsByTagName('DSUConfig'):
    for remote_sys in package_node.getElementsByTagName('System'):
        val = remote_sys.getAttribute("Address")
        ips.append(val)
print ips    
opmsg = op.split("\n")
print len(opmsg)
j = []
count = 0
for i in ips:
    print i,"###############################"
    found = False    
    for line in opmsg:
        if i in line and "Status" in line:
            count += 1
            found = True
        for j1 in j:
            if j1 in line:
                found = False
                break
        if found:
            with open(i+".txt","a+") as f0:
                f0.write(line+ "\n")
    j.append(i)

if len(ips) == count:
    print "both the count are equal"
else:
    print "both the count are different"
           
        
##aa = {}
##with open("100.100.40.245.txt","r") as f0:
##    for line in f0.readlines():
##        if "ReturnCode" in line:
##            line = line.strip()
##            print line.split("=")[1]
##            aa[1] = line.split("=")[1]
##print aa



