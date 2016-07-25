class Fruit:
	def __init__(self,price=0):
		self.price=price
	def __add__(self,other):
		return self.price+other.price
	def __gt__(self,other):
		if(self.price>other.price):
			flag=True
		else:
			flag=False
		return flag
class Apple(Fruit):
	pass
class Banana(Fruit):
	pass

if __name__ == '__main__':
	apple=Apple(3)
	banana=Banana(5)
	print ('apple price is %d,banana price is %d' % (apple.price,banana.price))
	print (apple>banana)
	total=apple+banana
	print ("total is %d" % total)