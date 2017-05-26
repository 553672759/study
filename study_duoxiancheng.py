#coding:utf-8
'''
2017年5月18日
@author: xx
'''
import thread
import time
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print "%s:%s" %(threadName,time.ctime(time.time()))


try:
    thread.start_new_thread(print_time, ("thread-1",1,))
    thread.start_new_thread(print_time, ("thread-2",2,))
    thread.start_new_thread(print_time, ("thread-3",3,))
    thread.start_new_thread(print_time, ("thread-4",4,))
    thread.start_new_thread(print_time, ("thread-5",5,))
    thread.start_new_thread(print_time, ("thread-6",6,))
    thread.start_new_thread(print_time, ("thread-7",7,))
    thread.start_new_thread(print_time, ("thread-8",8,))
    thread.start_new_thread(print_time, ("thread-9",9,))
    thread.start_new_thread(print_time, ("thread-10",10,))
    thread.start_new_thread(print_time, ("thread-11",9,))
    thread.start_new_thread(print_time, ("thread-12",8,))
    thread.start_new_thread(print_time, ("thread13",7,))
    thread.start_new_thread(print_time, ("thread-14",6,))
    thread.start_new_thread(print_time, ("thread-15",5,))
    thread.start_new_thread(print_time, ("thread-16",4,))
    
except:
    print "Error:unable to start thread"
    
while 1:
    pass