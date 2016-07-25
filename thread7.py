import threading
import time
class Counter:
	def __init__(self):
		self.value=0
		self.lock=threading.Lock()
	def increment(self):
		self.lock.acquire()
		self.value=self.value+1
		value=self.value
		self.lock.release()
		return value
counter =Counter()
class ThreadDemo(threading.Thread):
	def __init__(self,index,create_time):
		threading.Thread.__init__(self)
		self.index=index
		self.create_time=create_time
	def run(self):
		time.sleep(1)
		value=counter.increment()
		print ((time.time()-self.create_time),'\t',self.index,'\tvalue:',value)
for index in range(100):
	thread=ThreadDemo(index,time.time())
	thread.start()
