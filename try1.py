#!/usr/bin/python
# Filename: try1.py

number=23
t=True
while t:
	guess=int(input('Enter an integer:'))
	if guess == number:
		print('Congrtulations')
		print('(but you will not get anthing)')
		t=False
		
	elif guess > number:
		print('Higher')
	else:
		print('Lower')

else:
	print('Done and over.')
