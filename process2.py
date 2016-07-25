import subprocess
#pingP=subprocess.Popen(args='ping -c 4 www.sina.com.cn',shell=True)
pingP=subprocess.Popen(args='ping -c 4 www.sina.com.cn',shell=True,stdout=subprocess.PIPE)
pingP.wait()
#print (pingP.stdout.read())
print (pingP.pid)
print (pingP.returncode)

