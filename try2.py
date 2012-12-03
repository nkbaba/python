#!/usr/bin/python
# Filename:try2.py

while True:
	s=input('Enter something')
	if s=='quit':
		break
	if len(s)<3:
		print('Too small')
		continue
	print('Input is fine')

