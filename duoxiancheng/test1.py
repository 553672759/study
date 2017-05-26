# -*- coding:utf-8 -*-  
'''
Created on 2017��5��25��

@author: xx
'''
from threading import Thread  
from time import sleep
  
  

        
        
class MyThread(Thread):  
    def __init__(self):  
        Thread.__init__(self)    
        #super(MyThread, self).__init__()  
  
    def run(self):  
        #write this thread task 
        while True:
            sleep(5) 
            print self.__hash__()  
  
  
if __name__ == '__main__':  
    thread = MyThread()  
    thread.start()  
    #thread.join() 