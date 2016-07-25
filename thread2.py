import threading
import time
class ThreadSkeleton(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		print('a new thread---')
thread=ThreadSkeleton()
thread.start()
#time.sleep(2)
print ('hello,thread---')
