class Person:
	def __init__(self,name):
		self.name=name
	def say(self):
		print('Hello',self.name)

p= Person('Name')
p.say()
x= Person('Hi')
x.say()
