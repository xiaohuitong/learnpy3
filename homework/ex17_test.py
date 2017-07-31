from sys import argv

script,filename = argv

print "here is the content about %s" % filename
abs = open(filename)
print abs.read()

print "please import the name again"
file_again = raw_input('>')

data = open(file_again)
print data.read()
print "that's all,i will close it.thank you"
abs.close()
data.close()