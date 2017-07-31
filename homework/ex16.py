# -*- coding: utf-8 

from sys import argv 
script,filename = argv # 参数解包

print "we're going to erase %r." % filename 
print "if you don't want that,hit CTRL-C (^C)."
print "if you do want that,hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename,'w') # 打开一个写文件并赋给target

print 'truncateing the file.goodbye!'
target.truncate() # 删除文件中的所有内容

print "now i'm going to ask you for three lines."

line1 = raw_input("line1: ") # 输入内容并赋给line1
line2 = raw_input('line2: ')
line3 = raw_input('line3: ')

print "i'm going to write this to the file."

target.write(line1+'\n'+line2+'\n'+line3+'\n') # 用一个target.write（）把所有行的内容写进文件
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

print "and finally,we close it."
target.close()# 关闭文件


#如果你用 'w' 模式打开文件，那么你是不是还要target.truncate()呢？
# 不需要，因为‘w’在写之前，第一步就是要把文件清空。（'w':open for writing,truncaing the file first.）


