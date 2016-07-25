import os
#for key in os.environ.keys():
#	print (key,'\t',os.environ[key])
#print (os.system('dir'))
gedit='/usr/bin/gedit'
os.execl(gedit,'gedit')

