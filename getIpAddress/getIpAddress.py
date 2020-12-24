#!/bin/python
########################## Initialization #######################

from commonImports import *

from logLib import logLib
from commonLib import commonLib

logg = logLib()
clib = commonLib()

fname = "testlogging.txt"
logger = logg.startlogging(fname)

exit_code,output= clib.runcmd(logger, "ip address")

logg.stoplogging()
##################### Post Analysis #####################################
tt = open(fname, "r")
lines = tt.readlines()

pattern = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

ss = re.compile("inet.(.*)....brd")
ll = []
for line in lines:
	if ss.findall(line):
		output=re.search(pattern,line)
		if output:
			ll.append(output.group())
print(ll)
print("\nIP address is:")
print(ll[0])