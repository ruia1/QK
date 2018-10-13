# -*- coding: utf-8 -*-
#各モードを開くためのプログラム
from tkinter import *
import goropri,primalytest,gamemode,psearch,panalyze
def f1():
    qkh1.destroy()
    primalytest.pthome()
def f2():
    qkh1.destroy()
    psearch.sehome()
def f3():
    qkh1.destroy()
    goropri.gohome()
modes = [["素数判定モード","素数判定をします。",f1],
         ["素数探索モード","素数を様々な条件で探索できます。",f2],
         ["語呂モード","語呂素数の探索をします。",f3]]
class qkhc(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.createw()
    def createw(self):
        self.qkhlb = Label(self,text="進みたいモードのボタンを押してください。")
        self.qkhlb.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
        for i in range(3):
            self.qkhptestb = Button(self,text=modes[i][0],command = modes[i][2])
            self.qkhptestb.grid(row=i+1,column=0,padx=5,pady=5,sticky=W+E)
            self.qkhptestl = Label(self,text=modes[i][1])
            self.qkhptestl.grid(row=i+1,column=1,padx=5,pady=5,sticky=W)
        self.qkhexit = Button(self,text="終了",command = qkh1.destroy)
        self.qkhexit.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
        
def qkhome():
    qkh1 = Tk()
    qkh1.title="QK Supporter ホーム"
    qkh2 = qkhc(qkh1)
    qkh2.mainloop()
    