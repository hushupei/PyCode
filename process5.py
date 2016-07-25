import subprocess
import signal
def sigint_handler(signum,frame):
	print ('in signal SIGINT handler')
signal.signal(signal.SIGINT,sigint_handler)

while True:
	ret=input('Prompt>')
	print ('hello,',ret)

