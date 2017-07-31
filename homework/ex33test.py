number = int(input('number:'))
v = int(input('distance:'))
def num(number):
	i = 0
	lists = []
	while i<number:
		lists.append(i)
		i +=v
	print ('now the lists is:',lists)
	
	
num(number)
