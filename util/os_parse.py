import re
#sss = "Description:	Red Hat Enterprise Linux Server release 6.10 (Santiago)"
sss = "SUSE Linux Enterprise Server release 6.10"
print re.findall("SUSE Linux Enterprise Server .* ([0-9]*).[0-9]*",sss,re.IGNORECASE)[0]
