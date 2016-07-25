import _thread
import time
def worker(index,create_time):
	time.sleep(1)
	print((time.time()-create_time),'\t\t',index)
	print('Thread %d exit---' % (index))
	print(_thread.get_ident())
	_thread.exit()
for index in range(4):
	_thread.start_new_thread(worker,(index,time.time()))
time.sleep(20)
print ('main thread exit---')
