 # -*- coding: utf-8 
 
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ('one','two','three','four')
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
"i had this thing.",
"that you could type up right.",
"but it didn\'t sing",
"so i said goodnight.")

# 注意最后一行程序中既有单引号又有双引号，你觉得它是如何工作的？
# 在python中，双引号和单引号并没有本质的区别，但前后必须保持一致
# 如果引起冲突，要用反斜杠“\”，例如双引号中间可以允许单引号的存在，如果中间也是双引号，
# 就要在中间的双引号前面加上反斜杠，单引号也是一样。