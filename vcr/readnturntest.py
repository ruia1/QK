# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:39:42 2018

@author: tyyth
"""
class turn:
    def __init__(self,yourturn,draw = 0,p = 0,pfac = 0,bad = 0,penalty = 0,pas = 0):
        self.yourturn = yourturn
        self.draw = draw
        self.p = p
        self.pfac = pfac
        self.bad = bad
        self.penalty = penalty
        self.pas = pas
        
    def strp(self):
        if type(self.p) == int:
            return str(self.p)
        q = ""
        for i in self.p:
            q += i
        return q
    
    def strpfac(self):
        if type(self.pfac) == int:
            return str(self.pfac)
        qfac = ""
        for i in self.pfac:
            qfac += i
        return qfac
    
    def strpenalty(self):
        if type(self.penalty) == int:
            return str(self.penalty)
        ret = ""
        for i in self.penalty:
            ret += i
        return ret
    
    def output(self):
        l = str(self.yourturn)
        for i in list(map(str,[self.draw,self.strp(),self.strpfac(),self.bad,self.strpenalty(),self.pas])):
            l += "," + i
        return l
    
    def testout(self):
        print("yourturn:",self.yourturn)
        print("draw:",self.draw)
        print("p:",self.strp())
        print("pfac:",self.strpfac())
        print("bad:",self.bad)
        print("penalty:",self.strpenalty())
        print("pas:",self.pas)

def substitute(st):
    st = st.replace("+","")
    st = st.replace("=","")
    st = st.replace("10","T")
    st = st.replace("11","J")
    st = st.replace("12","Q")
    st = st.replace("13","K")
    st = st.replace("★","X")
    st = st.replace("∞","m")
    st = st.replace("pass","%")
    st = st.replace("bad,","")
    return st

def readnturn(yturn,n):
    if n == "lose":
        print("エラーです。コードrnt11")
        ret = turn(yturn)
        return ret
    if n == "-" or n == "pass":
        ret = turn(yturn,pas = 1)
        return ret
    i = 0
    n = substitute(n)
    nlen = len(n)
    draw = 0
    if n[0] != "[":
        draw = n[0]
        i += 2
        if n[2] == "%":
            ret = turn(yturn,draw = draw,pas = 1)
            return ret
    if n[i] != "[":
        print("エラーです。コードrnt12")
        ret = turn(yturn)
        return ret
    beg = i+1
    end = n.find("]")
    p = n[beg:end].split(sep = ",")
    i = end+2-yturn
    if i >= nlen:
        ret = turn(yturn,draw = draw,p = p)
        return ret
    pfac = 0
    if n[i] == "[":
        beg = i+1
        end = beg + n[beg:].find("]")
        pfac = n[beg:end].split(sep = ",")
        i = end + 2
    else:
        i += yturn
    if i >= nlen:
        ret = turn(yturn,draw = draw,p = p,pfac = pfac)
        return ret
    penalty = n[i:-2].split(sep=",")
    ret = turn(yturn,draw = draw,p = p,pfac = pfac,bad = 1,penalty = penalty,pas = 1)
    return ret

def r():
    ret = readnturn(1,input())
    ret.testout()
    print(ret.output())