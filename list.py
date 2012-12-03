x=0
def magic():
	global x
	
	while True:
		print()
		ch=input('Enter your number or quit for exit ')
		if ch == 'quit':
			break
		else:
			y=int(ch)
			x+=y
			print('The total is = ',x)
		
magic()
