class Fruit:
	pass

def Add(self):
	print ('grow...')

if __name__=="__main__":
	Fruit.grow=Add
	fruit=Fruit()
	fruit.grow()
