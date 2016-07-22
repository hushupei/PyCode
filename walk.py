import os,time
def showFileProperties(path):
	for root,dirs,files in os.walk(path,True):
		print('weizhi:'+root)
		for filename in files:
			state=os.stat(root+'/'+str(filename))
			info='name:'+filename+' '
			info=info+'size:'+('%d'% state[-4])+' '
			t=time.strftime('%Y-%m-%d %X',time.localtime(state[-1]))
			info=info+'create time:'+t+' '
			t=time.strftime('%Y-%m-%d %X',time.localtime(state[-2]))
			info=info+'change time:'+t+' '
			t=time.strftime('%Y-%m-%d %X',time.localtime(state[-3]))
			info=info+'access time:'+t+' '
			print(info)

if __name__ == '__main__':
	path=r'.'
	showFileProperties(path)

