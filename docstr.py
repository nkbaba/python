def doc(x):
	''' This is something
		Additionally this is also something that you really dont want to miss'''
	print('The value is ',x)
doc(5)
print(doc.__doc__)

import os
import sys
print('Directories are \n',sys.path,'\n')
print('\n\n',os.getcwd())
