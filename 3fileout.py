#readTextFile.py read and dsplay text readTextFile
#get file name
fname=raw_input('enter filename:')
print
#attempt to open file for reading
try:
	fobj=open(fname,'r')
except IOError,e:
	print '%s open error' % (fname),e
else:
	#display contents to the screen
	for line in fobj:
		print line,
	fobj.close()
	