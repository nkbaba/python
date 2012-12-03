shoplist=['a','b','f','c','d']
print('My shoplist is of :',len(shoplist),'I am going to buy',shoplist)

''' This is it'''

for listi in shoplist:
	print('\n',listi,end='')

shoplist.append('e')

print('\nNow ',shoplist)

shoplist.sort()

print('Now',shoplist)

del shoplist[0]

print('Now',shoplist)

a='g'

shoplist.append(a)

print('Now ',shoplist)

print('Now we can also see from 1 to 3',shoplist[0:2])

print('From 2 to end',shoplist[1:])

print('From 1 to -1',shoplist[1:-1])

print('Finish')
