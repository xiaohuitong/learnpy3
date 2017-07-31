from sys import argv

script,filename = argv

txt = open(filename)
print "there are the content about %r?" % filename
print txt.read()

b = raw_input('file_again: ')
filo =open(b)
print "there are the content about %r?" % b 
print filo.read()
print "now we have closed it"

txt.close()
filo.close()
