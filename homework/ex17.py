# -*- coding: utf-8
from sys import argv

#from os.path import exists

script,from_file,to_file = argv

#print "copying from %s to %s" % (from_file,to_file)

#in_file = open(from_file)
indata = open(from_file).read()

#print "the input file is %d bytes long" % len(indata)

#print "dose the output file exist? %r" % exists(to_file)
#print "really,hit return to continue,CTRL-C to abort"
#raw_input()

open(to_file,'w').write(indata)
#out_file.write(indata)

#print 'alright,all done'

#out_file.close()
#in_file.close()



#如果程序写成这样：indata = open(from_file).read()  
#这意味着你无需再运行``in_file.close()``了，
#因为read()一旦运行，文件就会被读到结尾并且被close掉

#close()作用：
#file.close()是为了释放资源，如果不close()，那就要等到垃圾回收时，自动释放资源。
#垃圾回收的时机是不确定的，也无法控制。如果程序是一个命令，很快就执行完了，那么可能就影响不大。
#但如果程序是一个服务，或是需要很长时间才能执行完，就可能导致资源被耗尽，也可能导致死锁。