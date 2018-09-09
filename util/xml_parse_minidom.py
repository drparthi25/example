import os
from xml.dom.minidom import parse, Document
import xml.etree.ElementTree as ET
import pdb
##pdb.set_trace()
def parse_xml(catalog):
        dom = parse(catalog)
        return dom

for node in parse("Catalog.xml").getElementsByTagName('PlatformCodes'):
        for platform in  node.getElementsByTagName("Platform"):
                if not platform.getAttribute("generation") == "PV":
                    print platform.getAttribute("name")

##for node in parse_xml("Catalog.xml").getElementsByTagName('SoftwareComponent'):
##    path=node.getAttribute('path').split('/')[-1]
##    relid = node.getAttribute('releaseID')
##    pack_type = node.getAttribute('packageType')
##    if relid not in pkgid:
##        pkgid[path] = pack_type+","+relid
####print pkgid
##
##for key,value in pkgid.items():
##    #pdb.set_trace()
##    #print release, pkgid[release]
##    if u'LW64' in value.split(',')[0] and u'LWXP' not in value.split(',')[0]:
##        #pdb.set_trace()
##        if key not in comp_list:
##            print key
##            missing_32bit_rel=key
##        

##def test_pass_verification():
##for filename in ["PIEConfig.xml","package.xml"]:
##    for PIEConfig_node in parse_xml(filename).getElementsByTagName('FMPWrappers'):
##            for node in PIEConfig_node.getElementsByTagName("FMPWrapperInformation"):
##                    PIEConfig_node_id =  node.getAttribute("identifier")
##    for package_node in parse_xml("package.xml").getElementsByTagName('FMPWrappers'):
##            for node in PIEConfig_node.getElementsByTagName("FMPWrapperInformation"):
##                    package_node_id = node.getAttribute("identifier")

##for node in parse_xml(filename).getElementsByTagName('SoftwareComponent'):
##        for info in node.getElementsByTagName('ImportantInfo'):
##                if info.hasAttribute("URL"):
##                        for dev in node.getElementsByTagName('Name'):
##                                compdisplay = dev.getElementsByTagName('Display')[0].firstChild.nodeValue
##                                print compdisplay



##def fmpvalue(root):
##        for val in root.findall('.//FMPWrappers//FMPWrapperInformation'):
##            fmpidentifier=val.attrib.get('identifier')
##            fmpwinfo=val.attrib
##            return (fmpidentifier,fmpwinfo)
##
##def Rbvalue(root,roote):
##         for val in root.findall('.//RollbackInformation'):
##                 rollbk_idfr=val.attrib.get('fmpWrapperIdentifier')
##                 if roote == rollbk_idfr:
##                         print 'One of the Rollback info mapped to fmpwrapperinfo with identifier %s'%rollbk_idfr
##                         Rbinfo = val.attrib
##                         return (rollbk_idfr,Rbinfo)


##def test_package_xml_verification():
##    try:
##
##            package_xml = 'package.xml'
##            pieconfig_xml = 'PIEConfig.xml'
##            tree,tree1 = ET.parse(pieconfig_xml),ET.parse(package_xml)
##            root,root1 = tree.getroot(),tree1.getroot()
##            if fmpvalue(root)==fmpvalue(root1):
##                print "Fmpwrapper information present in pie and package xml are same"
##            else:
##                print "Fmpwrapper mismatch found \n\t PIE values :"
##                #print self.fmpvalue(root),self.fmpvalue(root1)
##                        
##            if Rbvalue(root,fmpvalue(root)[0])==Rbvalue(root1,fmpvalue(root1)[0]):
##                print "Rollback information present in pie for matching identifier is present in package xml"
##                print "#######"
##            else:
##                print "Rollback mismatch found \n\t"
##                #print self.Rbvalue(root,self.fmpvalue(root)[0]),self.Rbvalue(root,self.fmpvalue(root1)[0])
##
##
##    except Exception as e:
##        print e
##        
##
##
##test_package_xml_verification()
##        
