Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> s="hello"
>>> for i in range(s.length,0,-1):
... 	s+=s[i]
... 	print "%d %s," % i,s[i]
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
>>> t=""
>>> s="hello"
>>> for i in range(s.length,0,-1):
... 	print "%d %s," % i,s[i]
... 	t+=s[i]
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
>>> for i in range(len(s),0,-1):
... 	print "%d %s," % i,s[i]
... 	t+=s[i]	
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: not enough arguments for format string
>>> s[3]
'l'
>>> t+s[3]
'l'
>>> t+=s[3]
>>> t 
'l'
>>> t+=s[4]
>>> t 
'lo'
>>> t=""
>>> for i in range(len(s),0,-1):
... 	t+=s[i]
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: string index out of range
>>> for i in range(len(s)-1,0,-1):
... 	t+=s[i]
... 
>>> t 
'olle'
>>> for i in range(len(s)-1,-1,-1):
... 	t+=s[i]
... 
>>> t 
'olleolleh'
>>> for i in range(len(s)-1,0,-1):
... 	t+=s[i]
... 
>>> t 
'olleolleholle'
>>> t =""
>>> for i in range(len(s)-1,-1,-1):
... 	t+=s[i]
... 
>>> t 
'olleh'
>>> import time,datetime
>>> print (time.strftime("%Y-%m-%d %X",time.localtime()))
2016-07-14 09:44:16
>>> t=time.strptime("2016-08-31","%Y-%m-%d")
>>> print (datetime.datetime(y,m,d=t[0:3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> print (datetime.datetime(t[0:3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: an integer is required
>>> y,m,d=t[0:3];print (datetime.datetime(y,m,d))
2016-08-31 00:00:00
>>> import re 
>>> s="HELLO WORLD"
>>> print (re.findall(r"^hello",s))
[]
>>> print (re.findall(r"^hello",s,re.I))
['HELLO']
>>> print (re.findall("^hello",s,re.I))
['HELLO']
>>> print (re.findall("WORLD",s,re.I))
['WORLD']
>>> print (re.findall("WORLD$",s,re.I))
['WORLD']
>>> print (re.findall("WORLD$",s))
['WORLD']
>>> print (re.findall("WOrLD$",s,re.I))
['WORLD']
>>> print (re.sub("hello","hi",re.I))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\re.py", line 151, in sub
    return _compile(pattern, flags).sub(repl, string, count)
TypeError: expected string or buffer
>>> print (re.sub("hello","hi",s))
HELLO WORLD
>>> print (re.sub("HELLO","hi",s))
hi WORLD
>>>  tel3=(010)12345678
  File "<stdin>", line 1
    tel3=(010)12345678
    ^
IndentationError: unexpected indent
>>>  tel3="(010)12345678"
  File "<stdin>", line 1
    tel3="(010)12345678"
    ^
IndentationError: unexpected indent
>>> tel3="(010)12345678"
>>> print (re.findall("[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}",tel3))
['(010)12345678']
>>> tel4=1234-5678987
>>> print (re.findall("[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}",tel4))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\re.py", line 177, in findall
    return _compile(pattern, flags).findall(string)
TypeError: expected string or buffer
>>> tel4="1234-2345678"
>>> print (re.findall("[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}",tel4))
['1234-2345678']
>>> print (re.findall("[\(]?\d{3}[\]-]?\d{8}|[\(]?\d{4}[\]-]?\d{7}",tel4))
['1234-2345678']
>>> print (re.findall("[\(]?\d{3}[\]-]?\d{8}|[\(]?\d{4}[\]-]?\d{7}",tel3))
[]
>>> print (re.findall("[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}",tel3))
['(010)12345678']
>>> 