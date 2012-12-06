#!/usr/bin/python
# Filename: backup2.py

import os
import time

source=input('Enter the location for backup');

while True:
	i=input('Do you want to add more location enter location or quit')
	if i=='quit':
		break
	else:
		source.append(i)

target_d=' /home/apurva/'

target=target_d+os.sep+time.strftime('%H%M%S')+'.zip'

print(os.sep)

print(time.strftime('%Y%m%d%H%M%S'))


zip_command="zip -qr {0} {1} ".format(target,''.join(source))

if os.system(zip_command) == 0:
	print('Success',target)
else:
	print('Failed')
