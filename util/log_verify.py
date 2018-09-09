import os
import re,pdb
from xml.dom.minidom import parse, Document
op = """ dsu]2;Administrator: Command Prompt - dsu[7;1HDELL EMC System Update 1.6.0[8;1HCopyright (C) 2014 DELL EMC Proprietary.[9;1HVerifying catalog installation ...[10;1HFetching Catalog ...[11;1HExtracting C:\Dell\DELL EMC System Update\dell_dup\Catalog.gz[12;1HReading the catalog ...[13;1HFetching invcol_VPJT7_WIN64_18_06_000_248_A00 ...[14;1HVerifying inventory collector installation ...[15;1HGetting System Inventory ...[16;1HDetermining Applicable Updates ...[17;1H[18;1H|--------DELL EMC System Update-----------|[19;1H[ ] represents 'not selected'[20;1H[*] represents 'selected'[21;1H[-] represents 'Component already at repository version (can be selected only if[22;1H /e option is used)'[23;1HChoose:  q - Quit without update, c to Commit, <number> - To Select/Deselect, a [24;1H- Select All, n - Select None [25;1H
[25;1H                                                                                [25;1H[ ]1 Dell 12Gbps SAS HBA Driver[25;1H
[25;1H                                                                                [25;1HCurrent Version : 2.51.12.80 Upgrade to : 2.51.21.1, Criticality : Recommended,[25;1H
[25;1H                                                                                [24;80H [25;1HType : Driver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]2 PERC H730 Adapter Controller 0 Firmware[25;1H
[25;1H                                                                                [25;1HCurrent Version : 25.5.2.0001 same as : 25.5.2.0001, Criticality : Recommended,[25;1H
[25;1H                                                                                [24;80H [25;1HType : Firmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]3 NVMePCISSD Model Number: Dell Express Flash NVMe PM1725 3.2TB AIC[25;1H
[25;1H                                                                                [25;1HCurrent Version : KPYABD3Q same as : KPYABD3Q, Criticality : Recommended, Type [25;1H
[25;1H                                                                                [24;80H:[25;1H Firmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]4 OS COLLECTOR 2.1[25;1H
[25;1H                                                                                [25;1HCurrent Version : 2.1 same as : 2.1, Criticality : Recommended, Type : Applicat[25;1H
[25;1H                                                                                [24;80Hi[25;1Hon[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[ ]5 Broadcom NetXtreme Driver Family[25;1H
[25;1H                                                                                [25;1HCurrent Version : 0.0.0 Upgrade to : 20.8.1, Criticality : Optional, Type : Dri[25;1H
[25;1H                                                                                [24;80Hv[25;1Her[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]6  iDRAC[25;1H
[25;1H                                                                                [25;1HCurrent Version : 2.60.60.60 same as : 2.60.60.60, Criticality : Recommended, T[25;1H
[25;1H                                                                                [24;80Hy[25;1Hpe : Firmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]7 [0010] Broadcom NetXtreme Gigabit Ethernet #4[25;1H
[25;1H                                                                                [25;1HCurrent Version : 20.8.4 same as : 20.8.4, Criticality : Optional, Type : Firmw[25;1H
[25;1H                                                                                [24;80Ha[25;1Hre[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]8 [0008] Broadcom NetXtreme Gigabit Ethernet #3[25;1H
[25;1H                                                                                [25;1HCurrent Version : 20.8.4 same as : 20.8.4, Criticality : Optional, Type : Firmw[25;1H
[25;1H                                                                                [24;80Ha[25;1Hre[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]9 [0006] Broadcom NetXtreme Gigabit Ethernet[25;1H
[25;1H                                                                                [25;1HCurrent Version : 20.8.4 same as : 20.8.4, Criticality : Optional, Type : Firmw[25;1H
[25;1H                                                                                [24;80Ha[25;1Hre[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]10 [0007] Broadcom NetXtreme Gigabit Ethernet #2[25;1H
[25;1H                                                                                [25;1HCurrent Version : 20.8.4 same as : 20.8.4, Criticality : Optional, Type : Firmw[25;1H
[25;1H                                                                                [24;80Ha[25;1Hre[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]11 Dell 32 Bit uEFI Diagnostics[25;1H
[25;1H                                                                                [25;1HCurrent Version : 4239A36 same as : 4239A36, Criticality : Optional, Type : App[25;1H
[25;1H                                                                                [24;80Hl[25;1Hication[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]12 PERC H730 Adapter Driver[25;1H
[25;1H                                                                                [25;1HCurrent Version : 6.604.6.0 same as : 6.604.06.00, Criticality : Recommended, T[25;1H
[25;1H                                                                                [24;80Hy[25;1Hpe : Driver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]13 13G SEP Firmware, BayID: 1[25;1H
[25;1H                                                                                [25;1HCurrent Version : 2.25 same as : 2.25, Criticality : Optional, Type : Firmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]14 OpenManage | iDRAC Service Module[25;1H
[25;1H                                                                                [25;1HCurrent Version : 3.2.0 same as : 3.2.0, Criticality : Optional, Type : Applica[25;1H
[25;1H                                                                                [24;80Ht[25;1Hion[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[ ]15 Intel(R) Chipset INF[25;1H
[25;1H                                                                                [25;1HCurrent Version : 0 Upgrade to : 10.1.2.77, Criticality : Recommended, Type : D[25;1H
[25;1H                                                                                [24;80Hr[25;1Hiver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]16 Intel(R) Gigabit 4P I350-t Adapter[25;1H
[25;1H                                                                                [25;1HCurrent Version : 18.0.17 same as : 18.0.17, Criticality : Recommended, Type : [25;1H
[25;1H                                                                                [24;80HF[25;1Hirmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]17 Intel(R) Gigabit 4P I350-t Adapter[25;1H
[25;1H                                                                                [25;1HCurrent Version : 18.0.17 same as : 18.0.17, Criticality : Recommended, Type : [25;1H
[25;1H                                                                                [24;80HF[25;1Hirmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]18 Intel(R) Gigabit 4P I350-t Adapter[25;1H
[25;1H                                                                                [25;1HCurrent Version : 18.0.17 same as : 18.0.17, Criticality : Recommended, Type : [25;1H
[25;1H                                                                                [24;80HF[25;1Hirmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]19 Intel(R) Gigabit 4P I350-t Adapter[25;1H
[25;1H                                                                                [25;1HCurrent Version : 18.0.17 same as : 18.0.17, Criticality : Recommended, Type : [25;1H
[25;1H                                                                                [24;80HF[25;1Hirmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]20 Intel Family of Server Adapter Drivers[25;1H
[25;1H                                                                                [25;1HCurrent Version : 18.0.0 same as : 18.0.0, Criticality : Recommended, Type : Dr[25;1H
[25;1H                                                                                [24;80Hi[25;1Hver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]21 Dell 12Gbps HBA Controller 0 Firmware[25;1H
[25;1H                                                                                [25;1HCurrent Version : 15.17.09.06 same as : 15.17.09.06, Criticality : Recommended,[25;1H
[25;1H                                                                                [24;80H [25;1HType : Firmware[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]22 BIOS[25;1H
[25;1H                                                                                [25;1HCurrent Version : 1.8.0 same as : 1.8.0, Criticality : Urgent, Type : BIOS[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]23 Firmware for  - Disk 0 in Backplane 1 of PERC H730 Adapter Controller 0 i[25;1H
[25;1H                                                                                [24;80Hn[25;1H Slot 7 [25;1H
[25;1H                                                                                [25;1HCurrent Version : VT33 same as : VT33, Criticality : Recommended, Type : Firmwa[25;1H
[25;1H                                                                                [24;80Hr[25;1He[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]24 Emulex OneConnect OCe14102-U1-D 2-port PCIe 10GbE CNA[25;1H
[25;1H                                                                                [25;1HCurrent Version : 9.2.3 same as : 9.2.3, Criticality : Optional, Type : Driver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H[-]25 Emulex OneConnect OCe14102-U1-D 2-port PCIe 10GbE CNA[25;1H
[25;1H                                                                                [25;1HCurrent Version : 9.2.3 same as : 9.2.3, Criticality : Optional, Type : Driver[25;1H
[25;1H                                                                                [25;1H
[25;1H                                                                                [25;1H
"""

##ec = re.findall("Exit Code:.*",op)
##print ec
##for i in ec:
##   print i.split(":")[-1].strip()
           
#comp_list =  op.split("\n")

comp_list =  re.findall(".*][0-9]+ .*",op)
file_name = ""
return_list = []
for line in comp_list:
    if "[ ]" in line:
       print line
       return_list.append(line)
print len(return_list) 



       
##        ec = line.split("|")[-1]               
##        ec = ec.split(":")[-1].strip()
##        if ec == "0":
##            print "pass"
##        else:
##            print "fail"



