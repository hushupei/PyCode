class Fruit:
	def __init__(self):
		self.name='apple'
		self.__color='red'
	def grow(self):
		print ('fruit growing---')

if __name__ == '__main__':
	fruit=Fruit()
	fruit.grow()
	print fruit.name
	print fruit._Fruit__color
	#print fruit.color
	print (fruit)
