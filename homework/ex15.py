# -*- coding: utf-8

from sys import argv

script,filename  = argv #unpack argv to script and filename
txt = open(filename) # 把打开的文件内容赋给txt
print "here's your file %r:" % filename 
print txt.read() #打印出txt中的filename内容
#用raw_input()函数再次输出file的内容
print "type the filename again:" 
file_again = raw_input('>')  #在‘>’后面输入文件名称

txt_again = open(file_again) # 把打开的文件内容赋给txt_again

print txt_again.read() # 打印出file_again的内容
txt.close() #关闭文件txt
txt_again.close()#关闭文件txt_again  

# 只用raw_input写这个脚本：
name = raw_input('please enter the file name:')
content = open(name)
print content.read()
content.close()


#用raw_input写这个脚本，想想那种得到文件名称的方法更好，以及为什么？
#两者各有各的好处，如果喜欢开始时就输入文件，就用argv,
#如果需要后面的提示输入，就用raw_input
#我更喜欢前者，可以在命令行开始处一次完成所有操作。



