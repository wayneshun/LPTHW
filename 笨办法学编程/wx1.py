#coding:utf8
import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor",size=(410,345))
wx.Button(win,label='open',pos=(245,5),size=(80,25))
wx.Button(win,label='save',pos=(325,5),size=(80,25))

wx.TextCtrl(win,pos=(5,5),size=(240,25))
wx.TextCtrl(win,pos=(5,35),size=(400,300),style=wx.TE_MULTILINE|wx.HSCROLL)

win.Show()
app.MainLoop()