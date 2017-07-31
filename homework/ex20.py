# -*- coding: utf-8

from sys import argv
script,input_file = argv

def print_all(f):# 定义函数
	print f.read()
	
def rewind(f):# 定义函数
	f.seek(0) # seek()的作用见note，主要是将文件游标移动到指定位置，然后对当前位置操作。
	
def print_a_line(line_count,f):# 定义函数
	print line_count,f.readline(),

#readline()函数返回的内容中包含文件本来就有的\n ，而print在打印时又会添加一个\n ，
#这样一来就会多出一个空行了。解决方法是在print语句结尾加一个逗号,这样print就
#不会把它自己的\n打印出来了。
	
current_file = open(input_file)# 打开文件input_file，并将内容赋给current_file
print "first,let's print the whole file\n"
print_all(current_file)#调用函数

print 'now let\'s rewind,kind of like a tape'
rewind(current_file)#调用函数

print "let's print three lines:" 
current_line = 1
print_a_line(current_line,current_file)#调用函数，下同
print_a_line(current_line+1,current_file)
print_a_line(current_line+2,current_file)

# '+='的用法及小脚本：
# x += y => x = x + y
x = 1
x += 1
print x

