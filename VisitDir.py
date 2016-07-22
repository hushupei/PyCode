import os
def VisitDir(path):
	li=os.listdir(path)
	print li
	for item in li:
		pathname=os.path.join(path,item)
		if not os.path.isfile(pathname):
			VisitDir(pathname)
		else:
			print pathname

if __name__=='__main__':
	path=r'./'
	VisitDir(path)

