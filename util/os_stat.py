import time
##print os.stat("inv.xml").st_size
from threading import Thread 
##import platform
##print platform.architecture()
##print platform.uname()
import multiprocessing
import Queue

dict1 = {u'100.100.40.80': [u'administrator', u'cm_123', u'Windows'],\
         u'100.100.40.239': [u'root', u'dell@123', u'Linux'],\
         u'100.100.40.238': [u'root', u'dell@123', u'Linux'],\
         u'100.100.40.237': [u'root', u'dell@123', u'Linux']}


def inventory_new(cal):
    print "welcome"
    time.sleep(5)
    cal = cal +"hello"
    exit(cal)
    
if __name__ == '__main__':
    c = 0
    jobs = []

    #for k,v in dict1.iteritems():
    for i in range(5):
        #if c <=4:
        #th = Thread(target=inventory_new,args=(k))
        print "c ==>",c
        th = multiprocessing.Process(target=inventory_new, args=(i,))
        jobs.append(th)
        th.start()
        print "thread started"
        #c +=1
            
        #if len(dict1) == c or c ==4:
        #    print "inside"
    result = []
    for th1 in jobs:
        th1.join()
        result.append(th1.exitcode)
        #for th1 in list1:
        #    print th1
    print result
      
