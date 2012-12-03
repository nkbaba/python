#!/usr/bin/python
# Filename: backup.py

import os
import time

source=['"/home/apurva/Documents"', ' /home/apurva/python']

target_d=' /home/apurva/'

target=target_d+os.sep+time.strftime('%H%M%S')+'.zip'

print(os.sep)

print(time.strftime('%Y%m%d%H%M%S'))


zip_command="zip -qr {0} {1} ".format(target,''.join(source))

if os.system(zip_command) == 0:
	print('Success',target)
else:
	print('Failed')
