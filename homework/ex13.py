# -*- coding: utf-8

from sys import argv
script,first,second,third,four = argv

print 'the script is called: ',script
print 'your first variable is:',first
print 'your second variable is:',second
print 'your third variable is:',third
print 'add one:',four
raw_input('your name:')
raw_input('your age:')

# 当给脚本四个以下的参数，会显示值错误，并提示需要三个值解包。
#将  raw_input  和  argv  一起使用：

script,name = argv

print 'the script is called: ',script
print "what is your name:%s" %name

password = raw_input( "please enter your password:")

print "ok,very good!"

# 接收更多参数：
script, myname,age,weight,height = argv

print 'the script is called:',script
print 'my name is:%r' % myname
print 'i am %r years old.' % age
print 'my weight is %r kg.' % weight
print 'my height is %r m' % height



