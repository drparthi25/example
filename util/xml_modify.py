import os
import re,pdb
import xml.etree.ElementTree as ET
tree = ET.parse('dsuconfig_invalid_ip.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
