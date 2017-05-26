# -*- coding:utf-8 -*-  
'''
Created on 2017��5��25��

@author: xx
'''

import thread 
from time import sleep
import time
import threading

def func():
    for i in range(5):
        print 'func'
        sleep(1)
        #thread.exit()

thread.start_new(func,())
lock =threading.Lock()
print lock.locked()
count =0
if lock.acquire():
    print lock.locked()
    count += 1
    lock.release()
    
time.sleep(6)

'''
线程锁总结
通过threading.Lock()创建现成锁,
然后通过lock.acquire()请求线程锁定,此时被放入线程池,
如果获得锁定之后,则被激活,继续执行
'''
