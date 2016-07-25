import subprocess
import signal
def sigint_handler(signum,frame):
	print ('in signal SIGINT handler')
signal.signal(signal.SIGINT,sigint_handler)

pingP=subprocess.Popen(args='ping -c 4 www.sina.com.cn',shell=True)
pingP.wait()
print(pingP.pid)
print(pingP.returncode)

