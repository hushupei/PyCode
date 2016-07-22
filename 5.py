Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import glob
>>> import sys
>>> import os.path
>>> glob.glob("./*.txt")
['.\\fileinput.txt', '.\\hello2.txt', '.\\hello3.txt', '.\\helloworld.txt', '.\\unicode.txt']
>>> f1=file('hello2.txt','r')
>>> content=f1.read()
>>> print content
hello world
hello china

>>> f1.close()
>>> f1=file('hello2.txt','r')
>>> f2=file('hello.txt','w')
>>> for s in f1.readlines():
... 	f2.write(s)
... 	
... 
>>> f1.colse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'file' object has no attribute 'colse'
>>> f1.close()
>>> f2.close()
>>> import configparser
>>> config=configparser.ConfigParser()
>>> config.read('ODBC.ini')
[]
>>> 