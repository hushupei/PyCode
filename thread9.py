import time
import threading

class Goods:
	def __init__(self):
		self.count=0
	def produce(self,num=1):
		self.count+=num
	def consume(self):
		if self.count>0:
			self.count-=1
	def isEmpty(self):
		return not self.count
class Producer(threading.Thread):
	def __init__(self,condition,goods,name,sleeptime=1):
		threading.Thread.__init__(self)
		self.cond=condition
		self.goods=goods
		self.sleeptime=sleeptime
		self.name=name
	def run(self):
		cond=self.cond
		goods=self.goods
		while True:
			cond.acquire()
			goods.produce()
			print('goods count:',goods.count,'producer--- '+self.name)
			cond.notifyAll()
			cond.release()
			time.sleep(self.sleeptime)

class Consumer(threading.Thread):
	def __init__(self,index,condition,goods,name,sleeptime=4):
		threading.Thread.__init__(self)
		self.cond=condition
		self.goods=goods
		self.sleeptime=sleeptime
		self.name=name
	def run(self):
		cond=self.cond
		goods=self.goods
		while True:
			time.sleep(self.sleeptime)
			cond.acquire()
			while goods.isEmpty():
				cond.wait()
			goods.consume()
			print('goods count:',goods.count,'consumer '+self.name)
			cond.release()

threads=[]
goods=Goods()
cond=threading.Condition()
for i in range(2):
	producer=Producer(cond,goods,str(i))
	producer.start()
	threads.append(producer)
for i in range(5):
	consumer =Consumer(i,cond,goods,str(i),2)
	consumer.start()
	threads.append(consumer)
for thread in threads:
	thread.join()




			
