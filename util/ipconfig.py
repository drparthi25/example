import subprocess
cmd = "ipconfig"
op,err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print op
print "error",  err
import platform
print platform.uname()[4]
print platform.uname()
import socket
print socket.gethostbyname(socket.gethostname())

