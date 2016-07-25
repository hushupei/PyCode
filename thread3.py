import threading
import time
class ThreadDemo(threading.Thread):
	def __init__(self,index,create_time):
		threading.Thread.__init__(self)
		self.index=index
		self.create_time=create_time
	def run(self):
		self.setName('Thread-'+str(self.index))
		print('Thread %s runing---' % (self.getName()))
		time.sleep(1)
		print((time.time()-self.create_time),'\t',self.index)
		print('Thread %d exit---' % (self.index))
for index in range(5):
	thread=ThreadDemo(index,time.time())
	thread.start()
#time.sleep(20)
print ('main thread exit---')
