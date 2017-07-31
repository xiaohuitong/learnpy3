# -*- coding: utf-8

print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print 'how much do you weight?',
weight = raw_input()

print "so,you are %r old,%r tall and %r height." %(age,height,weight)


# my example:
name = raw_input("your name is: ")
print "hi,%r,good morning!" % name

# 想想为什么最后一行  '6\'2"'  里边有一个  \'  序列?
# 单引号需要被转义，从而防止它被识别为字符串的结尾