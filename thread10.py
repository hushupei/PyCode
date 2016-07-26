import time,random
import threading

class Consumer(threading.Thread):
	def __init__(self,sema,name):
		threading.Thread.__init__(self)
		self.sema=sema
		self.name=name
	def run(self):
		sema=self.sema
		while True:
			sleeptime=random.choice(range(5))
			time.sleep(sleeptime)
			sema.acquire()
			print('consumer '+self.name+' using')
			print('resource releasing---')
			sema.release()

max_res=3
res_sema=threading.Semaphore(value=max_res)
threads=[]
for i in range(10):
	consumer =Consumer(res_sema,str(i))
	consumer.start()
	threads.append(consumer)
for thread in threads:
	thread.join()




			
