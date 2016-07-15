from __future__ import division
import myModule 

#myModule.func()
#myClass=myModule.MyClass()
#myClass.myFunc()
print (__doc__)
print (__file__)
print (__name__)
print (__package__)
#print (__loader__) #not exist
def ffunc(x):
	if x>0:
		return x
def sfunc(x,y):
	return x+y

def mfunc(x,y):
	return x*y
 
print (filter(ffunc,range(-5,5)))
print (reduce(sfunc,range(1,5)))
print (reduce(mfunc,range(1,5)))

def power2(x,y):return x**y
print (map(power2,range(1,5),range(5,1,-1)))
print (list(map(power2,range(1,5),range(5,1,-1))))



def oper(x=1,y=2,operator="+"):
	res={"+":x+y,"-":x-y,"*":x*y,"/":x/y}
	return res.get(operator)
print(oper(2,3,"-"))
print(oper(5,6,"/"))
print(oper(y=2,operator="*"))
print(oper(x=6))
print (oper(operator="*"))

dt={"one"=1,"two"=2,"three"=3}
print (dt.keys())
print (dt.values())
