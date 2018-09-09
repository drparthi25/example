import json
from xml.dom.minidom import parse
sys_info = []
os_info = []
system_info = {}
for node in parse("Catalog.xml").getElementsByTagName("SoftwareBundle"):
    #print node.getElementsByTagName("Model")
    os = " "
    sys_id=" "
    for os_node in node.getElementsByTagName("OperatingSystem"):
        #print node.getElementsByTagName("OperatingSystem")
        os =  node.getElementsByTagName("OperatingSystem")[0].getAttribute("osCode")
        os_info.append(os)
    for os_node in node.getElementsByTagName("Model"):
        sys_id =  node.getElementsByTagName("Model")[0].getAttribute("systemID")
    sys_info.append(sys_id+"_"+os)
    system_info[sys_id] = os
with open("catalog_json","w") as f0:
    json.dump(system_info,f0)
with open("catalog_json","r") as f1:
    json_data = json.load(f1)
    print json_data["06EE"]
print system_info
print set(os_info)
print len(sys_info)
print len(set(sys_info))

