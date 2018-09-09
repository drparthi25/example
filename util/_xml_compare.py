from sys import path as syspath
from os import getcwd as osgetcwd
import os,glob
syspath.append(osgetcwd())
import threading,time
import re,time,traceback,pickle
from datetime import datetime
from xlrd import open_workbook
from ConfigParser import ConfigParser
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import sys
import time
import string




controller_search = "h200","h700","h800","h310","h710","h810","h330","h730","h830","h740","h74p"
inv_parse=parse("inv.xml")
lcl_parse=parse("LCLRecords.xml")
device_node=lcl_parse.getElementsByTagName("Device")
inv_node=inv_parse.getElementsByTagName("Device")
lcl_inv_list=[]
ic_inv_list=[]
flag=0
for node in device_node:
    lcl_inv_list.append(node.getAttribute("display"))
print "Inventory from LCL Utility"
print lcl_inv_list
print "***********************************************************************************"

for node in inv_node:
    for app_node in node.getElementsByTagName("Application"):
        if app_node.getAttribute("componentType")=="DRVR":
            pass
        else:
            ic_inv_list.append(node.getAttribute("display"))
print "Inventory from IC"
print ic_inv_list
print "***********************************************************************************"
pass_flag=0


controller_comp_lcl=[]
controller_comp_ic=[]
for i in lcl_inv_list:
    for j in controller_search:
        #if re.findall(j,i.lower()):
        if j in i.lower():
            controller_comp_lcl.append(i)
if controller_comp_lcl:
    controller_comp_lcl = list(set(controller_comp_lcl))
    flag=1
    print "Storage Controller card is present in the SUT"
    print controller_comp_lcl

if flag==1:
    for j in controller_search:
        for i in ic_inv_list:
        
            if j in i.lower():
            #if re.findall(j,i.lower()):
                controller_comp_ic.append(i)
else:
    print "Storage controller Card is not present in the config"

if controller_comp_ic:
    controller_comp_ic = set(controller_comp_ic)
    print list(controller_comp_ic)
    pass_flag=1

if pass_flag==1:
    print "Storage Controller card is getting inventoried in the IC"
else:
    print "Storage Controller card is not getting inventoried in the IC"
    
if not len(controller_comp_ic)==len(controller_comp_lcl):
    print "Controller in lclutility file %s"%controller_comp_lcl 
    print "Controller in inventory file %s"%controller_comp_ic
    print "Same number of controller cards is not inventoried in lcl and IC"



















