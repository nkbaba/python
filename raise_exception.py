class shortInput(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast

try:
	text=input('Enter text :')
	if len(text) < 3:
		raise shortInput(len(text),3)

except EOFError:
	print('EOF')
except KeyboardInterrupt:
	print('Keyboard Terminate')
except shortInput as ex:
	print('Short Length'.format(ex.length, ex.atleast))
else:
	print('No exception')

