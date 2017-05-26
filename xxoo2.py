# -*- coding:utf-8 -*-  
'''
Created on 2017年5月24日

@author: xx
'''
import urllib2
import cookielib
import random
import socket

url="https://btso.pw/search/sis"

class BrowserBase(object): 
    
    def __init__(self):
        socket.setdefaulttimeout(20)
        self.page= ''
        self.articleName = ''
        self.link = ''
      
    def speak(self,name,content):
        print '[%s]%s' %(name,content)
    
    def getpage(self,url):
        cookie_support=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self.opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)
        user_agents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36']
        self.opener.addheaders=[("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
                                ("Accept-Language","zh-CN,zh;q=0.8"),
                                ("Host","btso.pw"),
                                ("User-Agent",user_agents)
                                ]
        try:
            response=self.opener.open(url)
            return response.read()
            
        except Exception,e:
            self.speak(str(e),url)
            raise Exception
        else:
            return response
        
        
if __name__=="__main__":
    splider=BrowserBase()
    page=splider.openurl("https://btso.pw/search/sis")

