the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'diems',3,'quarters']

#this first kind of for-loop goes through a list.
for number in the_count:
	print 'this is count %d' %number
	
# same as above 
for fruit in fruits:
	print 'a fruit of type: %s' %fruit
	
# also we can gothrough mixed list too.
# notice we have to use %r ,since we do not know what's in it 
for i in change:
	print 'i got %r' %i
	
# we can also build lists,first start with an empty one
elements = range(6)
# then we use the range function to do 0 to 5 counts.
#for i in range(6):
#	print 'adding %d to the list.' %i 
#	elements.append(i)
	
# now we can print them out too
for i in elements:
	print 'element was: %d' %i