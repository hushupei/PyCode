import threading
import time,random
class ThreadDemo():
	def __init__(self):
		self.local=threading.local()
	def run(self):
		time.sleep(random.random())
		self.local.number=[]
		for i in range(10):
			self.local.number.append(random.choice(range(10)))
		print (threading.currentThread(),self.local.number)
threadDemo=ThreadDemo()
threads=[]
for index in range(5):
	t=threading.Thread(target=threadDemo.run)
	t.start()
	threads.append(t)
#for thread in threads:
#	thread.join()
for i in range(5):
	threads[i].join()
print ('main thread exit---')
