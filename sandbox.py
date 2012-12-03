def total(initial=5, *numbers, **keywords):
	count=initial
	print()
	print('Initial and count',initial,count)
	for number in numbers:
		print('number and count :',number,count)
		count+=number
	for key in keywords:
		print('keyword and count and key',keywords[key],count, key)
		count+=keywords[key]
	return count

print(total(10,1,2,3,vegetables=50,fruits=100))
