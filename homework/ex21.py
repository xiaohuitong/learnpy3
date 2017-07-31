# -*- coding: utf-8 

def add(a,b):
	print 'adding %d +%d' % (a,b)
	return a+b
	
def subtract(a,b):
	print 'subtracting %d - %d' % (a,b)
	return a-b
	
def multiply(a,b):
	print "multiplying %d * %d" % (a,b)
	return a*b	
def divide(a,b):
	print "dividing %d/%d" % (a,b)
	return a/b
	
print "let't do some math with just function"
	
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "age: %d,height: %d,weight: %d,iq: %d" %(age,height,weight,iq)

#a puzzle for the extra credit,type it in anyway.
print 'here is a puzzle'

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "that becomes: ",what,"can you do it by hands?"


# return 和 print的区别小脚本：
def add(a,b):
    print a+b
    return a+b
		
a = 1
b = 2
add(a,b)
print add(a,b)
#正常方法实现谜题：
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

a = divide(iq,2)
b = multiply(weight,a)
c = subtract(height,b)
d = add(age,c)
print d
#颠倒过来计算一个简单的等式：
equation = 23 + 50 * (35-5)/6

x = subtract(35,5)
y = multiply(50,x)
z = divide(y,6)
w = add(23,z)
 
print 'the answer for the equation is:',w

