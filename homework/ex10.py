# -*- coding: utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# 使用  ''' ( 三个单引号 ) 取代三个双引号"""，效果是一样的.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


while True:
	for i in ['/','-','|','\\','|']:
		print "%s\r" % i,

#  用%r 搭配单引号和双引号转义字符打印一些字符串出来：		
print "it\'s an expensive book,don\'t %r it " % 'break'

