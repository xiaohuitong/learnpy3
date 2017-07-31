# -*- coding: utf-8

from sys import argv
# 
script,user_name = argv
prompt = '> '
print "hi %s,i'm the %s script." % (user_name,script)
print "i'd ike to ask you a few questions."
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)


print "what kind of computer do you have?"
computer = raw_input(prompt)

print '''
alright,so you said %r about liking me.
you live in %r. not sure where that is.
and you have a %r computer.nice.
''' % (likes,lives,computer)


# 改变prompt变量的内容，添加了一个参数：
script,user_name，sport= argv

prompt = 'you should enter something: '
print "hi %s,i'm the %s script." % (user_name,script)
print "i'd ike to ask you a few questions."
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)


print "what kind of computer do you have?"
computer = raw_input(prompt)

print 'about sport,last time you said you like %s ? ' %sport
sports = raw_input('please enter the name of sport:')

print '''
alright,so you said %r about liking me.
you live in %r. not sure where that is.
and you have a %r computer.and you said you like %r .nice.
''' % (likes,lives,computer,sports)