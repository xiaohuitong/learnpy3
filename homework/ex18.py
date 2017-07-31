# this one is like your scripts with argv
def print_two(*args):
	arg1,arg2 = args
	print "arg1: %r,arg2: %r" %(arg1,arg2)
	
# ok,that *arg is actually pointless,we can just do it.
def print_two_again(arg1,arg2):
	print "arg1: %r,arg2: %r" %(arg1,arg2)
	
# this is just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
    	
#this one takes no arguments
def print_none():
	print "i got nothing."

print_two('xing','ming')
print_two_again('xiao','huitong')
print_one('firt')
print_none()