# We are defining class here
class Robot:

	population = 0
	
	#Defining method almost like constructor in Java
	def __init__(self,name):
		self.name=name
		print('(Initializing {0})'.format(self.name))

		Robot.population +=1
	def __del__(self):
		print('{0} is now distroyed'.format(self.name))
		Robot.population -= 1
	
		if Robot.population==0:
			print('{0} was the last'.format(self.name))
		else:
			print('There are still {0:d} robots working'.format(Robot.population))

	def hi(self):
		print('Greeting from {0}'.format(self.name))

	def how():
		print('We have objects {0:d}'.format(Robot.population))

	how=staticmethod(how)


#main program starts here just like the main method in C++ or Java

droid1= Robot('R2-D2') #calling constructor
droid1.hi()

Robot.how()

two= Robot('Apurva')
two.hi()
Robot.how()

print('\nSomething is to learn\n')

print('Now distroy the obj')

del droid1
del two

Robot.how()

