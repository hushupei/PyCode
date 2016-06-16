a=0;
alist=[1,2,3,4,5,6,7,8,9]
aTuple=('1.sum','2.average','3.exit')

for opt in aTuple:
	print opt,
while(True):
	a=int(raw_input('choose a number(1,2,3)'))
	if 1<=a<=3:
		if a==1:
			print 'sum of alist is',sum(alist[0:])
		elif a==2:
			print 'average of alist is',sum(alist)/9.0
		else :
			break




