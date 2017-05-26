# -*- coding:utf-8 -*-  
'''
Created on 2017年5月24日

@author: xx
'''
import urllib2
import cookielib
import random
import socket
from bs4 import BeautifulSoup


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
        
    def get_links(self,BS_page):
        links=[]
        content=BS_page.find(class_='data-list')
        link=content.find_all('a')
        for i in link:
            links.append(i.get('href'))
        
        return links
    
    def get_detail(self,links):
        detail=[]
        num=1
        for i in links:
            page=self.getpage(i)
            BSpage=BeautifulSoup(page,'html.parser')
            title=BSpage.find("h3").get_text()
            link=BSpage.find("textarea",id="magnetLink").get_text()
            data={}
            data['num']=num
            num+=1
            data['title']=title
            data['link']=link
            detail.append(data)
            
        return detail
    
    def output_html(self,datas):
        fout=open('output.html','wb')
        
        fout.write("<html>")
        fout.write('<meta http-equiv="Content-type" content="text/html;charset=utf-8" />')
        fout.write('<head><title></title><script>')
        fout.write('function copyUrl()  {')
        fout.write('var url = document.getElementById("aa").href;')
        fout.write('window.clipboardData.setData("Text",url);')
        fout.write('alert("已复制链接");')
        fout.write(' } </script></head>')
        fout.write("<body>")
        fout.write("<table border='1'>")
        
        for data in datas:
            fout.write("<tr>")
            fout.write("<td>&nbsp;%s&nbsp;</td>"%data['num'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>>%s</td>"%data['link'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        
if __name__=="__main__":
    splider=BrowserBase()
    page=splider.getpage("https://btso.pw/search/sis")
    #print page
    BSpage=BeautifulSoup(page,'html.parser')
    links=splider.get_links(BSpage)
    detail=splider.get_detail(links)
    #print detail
    splider.output_html(detail)
    
    

