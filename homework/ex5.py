# -*- coding: utf-8
my_name = 'xiao huitong' # 赋值语句，把‘=’后面的内容赋给左边的变量
my_age = 35
my_height = 74
my_weight = 150
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print 'let\'t talk about %s' % my_name
print "he's %d inches tall" % my_height
print "he's %d pounds heavy" % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)

# 修改所有的变量名字，把它们前面的 ``my_`` 去掉，并且使用%r
name = 'xiao huitong' # 赋值语句，把‘=’后面的内容赋给左边的变量
age = 35
height = 74
weight = 150
eyes = 'black'
teeth = 'white'
hair = 'black'

print 'let\'t talk about %r' % name
print "he's %r inches tall" % height
print "he's %r pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth
print "If I add %r, %r, and %r I get %r." % (
age, height, weight, age + height + weight)


a = 1
print "%r(in) = %r(cm)" % (a,a*2.54)# 英寸换算成厘米
print "%r(lb) = %r(kg)" % (a,a*0.4536)#磅换算成千克


