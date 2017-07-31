# -*- coding: utf-8

def cheese_and_crackers(cheese_count,boxes_of_crackers):# 定义函数cheese_and_crackers
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes of crackers!" % boxes_of_crackers
	print "man that is enough for a party"
	print 'get a blanket.\n'
	
print 'we can just give the function numbers directly:'
cheese_and_crackers(20,30)

print 'or,we can use variable from our script:'
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print 'we can even do math inside too:'
cheese_and_crackers(10+20,5+6)

print 'and we can combine the two,variables and math:'
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
#怎样处理用户输入的数字:
b = int(raw_input('number: '))
c = int(raw_input('number2: '))
cheese_and_crackers(b,c)

# 自己编的函数：
def my_func(a,b):
    print a+b
#-----------------------
from sys import argv
script,x,y = argv 
a = int(x)
b = int(y)
my_func(a,b)
#-------------------------	
b = int(raw_input('number: '))
c = int(raw_input('number2: '))
my_func(b,c)
#----------------------
my_func(24,34)
#-------------------------
x = 4
y = 3
my_func(x,y)
#-------------------------
my_func(x+1,y+3)

#........
	