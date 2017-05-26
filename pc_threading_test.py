#coding:utf8
'''
Created on 

@author: xx
'''

import threading
import time,random,sys
from __builtin__ import type

class Counter:
    def init(self):
        self.lock=threading.Lock()
        self.value=0
    
    def increment(self):
        self.lock.acquire()
        self.value=value=self.value+1
        self.lock.release()
        return value

counter=Counter()
cond=threading.Condition()

class Worker(threading.Thread):
    
    def run(self):
        print self.getName(),"-- created."
        cond.acquire()
        cond.wait()
        cond.release()
        
if __name__=="__main__":
    try:
        for i in range(3500):
            Worker().start()
    except BaseException,e:
        print "异常",type(e),e
        time.sleep(5)
        print "maxium i =",i
    finally:
        cond.acquire()
        cond.notifyAll()
        cond.release()
        time.sleep(3)
        print threading.currentTheme().getName()," quit"
    
    
    