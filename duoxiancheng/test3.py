# -*- coding:utf-8 -*-  
'''
Created on 2017��5��25��

@author: xx
'''
import threading
import time

def context(tJoin):
    print 'in threadContext.'
    tJoin.start()
    tJoin.join(3)
    print 'out threadContext.'

def join():
    print 'in threadJoin.'
    time.sleep(3)
    print 'out threadJoin.'

tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()


'''
    总结一下start和join方法:
    通过threading.Thread(target=方法名,args=(方法参数1,方法参数2,))方法创建一个线程,
  当掉啊用start()方法时,现成才会启动,开始执行.
    当出现join()方式时,如果未设置指定时间,则会先阻塞当前方法,执行新的线程,
直到新线程执行完毕后才恢复.
如果设置了等待时间,到时间后会放开阻塞,继续当前线程,新的线程将继续执行.
    
'''