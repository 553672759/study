#coding:utf8

import wx
class MyApp(wx.App):
    def OnInit(self):
        #frame=wx.Frame(None,title="Hello,python")
        #frame.Show()
        return True
    
#带有输入框的Frame
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="hello",pos=(400,200),size=(700,400))
        self.panel=wx.Panel(self)
        #text1=wx.TextCtrl(panel,value="hello,python",size=(200,100))
        self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick)
    #当鼠标左键点击弹起时发生的事件    
    def OnClick(self,event):
        posm=event.GetPosition()
        wx.StaticText(parent=self.panel,label="hello",pos=(posm.x,posm.y))
        
if __name__=='__main__':
    app=MyApp()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()
    




