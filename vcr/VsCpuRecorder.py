# -*- coding: utf-8 -*-ｓ
import csv
#import tkinter as tk
#from tkinter import messagebox as tkm
#from tkinter import filedialog as tkf
games = []
eznum = [['TT', 'TJ', 'TQ', 'TK', 'TX', 'JJ', 'JQ', 'JK', 'JX', 'QQ', 'QK', 'QX', 'KK', 'KX', 'XX'],
['TTT', 'TTJ', 'TTQ', 'TTK', 'TTX', 'TJJ', 'TJQ', 'TJK', 'TJX', 'TQQ', 'TQK', 'TQX', 'TKK', 'TKX', 'TXX', 'JJJ', 'JJQ', 'JJK', 'JJX', 'JQQ', 'JQK', 'JQX', 'JKK', 'JKX', 'JXX', 'QQQ', 'QQK', 'QQX', 'QKK', 'QKX', 'QXX', 'KKK', 'KKX', 'KXX'],
['TTTT', 'TTTJ', 'TTTQ', 'TTTK', 'TTTX', 'TTJJ', 'TTJQ', 'TTJK', 'TTJX', 'TTQQ', 'TTQK', 'TTQX', 'TTKK', 'TTKX', 'TTXX', 'TJJJ', 'TJJQ', 'TJJK', 'TJJX', 'TJQQ', 'TJQK', 'TJQX', 'TJKK', 'TJKX', 'TJXX', 'TQQQ', 'TQQK', 'TQQX', 'TQKK', 'TQKX', 'TQXX', 'TKKK', 'TKKX', 'TKXX', 'JJJJ', 'JJJQ', 'JJJK', 'JJJX', 'JJQQ', 'JJQK', 'JJQX', 'JJKK', 'JJKX', 'JJXX', 'JQQQ', 'JQQK', 'JQQX', 'JQKK', 'JQKX', 'JQXX', 'JKKK', 'JKKX', 'JKXX', 'QQQQ', 'QQQK', 'QQQX', 'QQKK', 'QQKX', 'QQXX', 'QKKK', 'QKKX', 'QKXX', 'KKKK', 'KKKX', 'KKXX'],
['TTTTJ', 'TTTTQ', 'TTTTK', 'TTTTX', 'TTTJJ', 'TTTJQ', 'TTTJK', 'TTTJX', 'TTTQQ', 'TTTQK', 'TTTQX', 'TTTKK', 'TTTKX', 'TTTXX', 'TTJJJ', 'TTJJQ', 'TTJJK', 'TTJJX', 'TTJQQ', 'TTJQK', 'TTJQX', 'TTJKK', 'TTJKX', 'TTJXX', 'TTQQQ', 'TTQQK', 'TTQQX', 'TTQKK', 'TTQKX', 'TTQXX', 'TTKKK', 'TTKKX', 'TTKXX', 'TJJJJ', 'TJJJQ', 'TJJJK', 'TJJJX', 'TJJQQ', 'TJJQK', 'TJJQX', 'TJJKK', 'TJJKX', 'TJJXX', 'TJQQQ', 'TJQQK', 'TJQQX', 'TJQKK', 'TJQKX', 'TJQXX', 'TJKKK', 'TJKKX', 'TJKXX', 'TQQQQ', 'TQQQK', 'TQQQX', 'TQQKK', 'TQQKX', 'TQQXX', 'TQKKK', 'TQKKX', 'TQKXX', 'TKKKK', 'TKKKX', 'TKKXX', 'JJJJQ', 'JJJJK', 'JJJJX', 'JJJQQ', 'JJJQK', 'JJJQX', 'JJJKK', 'JJJKX', 'JJJXX', 'JJQQQ', 'JJQQK', 'JJQQX', 'JJQKK', 'JJQKX', 'JJQXX', 'JJKKK', 'JJKKX', 'JJKXX', 'JQQQQ', 'JQQQK', 'JQQQX', 'JQQKK', 'JQQKX', 'JQQXX', 'JQKKK', 'JQKKX', 'JQKXX', 'JKKKK', 'JKKKX', 'JKKXX', 'QQQQK', 'QQQQX', 'QQQKK', 'QQQKX', 'QQQXX', 'QQKKK', 'QQKKX', 'QQKXX', 'QKKKK', 'QKKKX', 'QKKXX', 'KKKKX', 'KKKXX']]
class game:
    def __init__(self,turnlen,turns,yfirst,ywin,yhand,chand,yez=0,cez=0):
        self.turnlen = turnlen
        self.turns = turns
        self.yfirst = yfirst
        self.yhand = self.sethand(yhand)
        self.chand = self.sethand(chand)
        self.ywin = ywin
        self.yez = yez
        self.cez = cez
    
    def sethand(self,hand):
        hand = sorted(hand[0:-1])
        tjstr,hcount,tjlis = self.sortez(hand)
        hnum = hand[0:len(hand)-hcount-1]
        hnum.extend([x for x in tjstr])
        return hnum
    
    def setez(self):
        self.yez = self.calez(self.yhand)
        self.cez = self.calez(self.chand)
        
    def sortez(self,hand):
        tjlis = [hand.count("T"),hand.count("J"),
                 hand.count("Q"),hand.count("K"),hand.count("X")]
        hcount = sum(tjlis)
        tjstr = ""
        for i in range(5):
            tjstr += tjlis[i] * ["T","J","Q","K","X"][i]
        return [tjstr,hcount,tjlis]
    
    def calez(self,hand):
        tjstr,hcount,tjlis = self.sortez(hand)
        if hcount >= 7:
            return hcount+228
        elif hcount == 6:
            return tjlis[1]+tjlis[3]+tjlis[4]+228
        elif hcount == 0:
            return 1
        elif hcount == 1:
            for i in range(5):
                if tjlis[i] == 1:
                    return i+2
        else:
            global eznum
            if hcount == 2:
                return 7 + eznum[0].index(tjstr)
            elif hcount == 3:
                return 22 + eznum[1].index(tjstr)
            elif hcount == 4:
                return 56 + eznum[2].index(tjstr)
            else:
                return 121 + eznum[3].index(tjstr)
            
    def outhand(self,hand):
        ret = ""
        for i in hand:
            ret += i
        return ret
    def output(self,outfile):
        self.setez()
        l = str(self.turnlen)
        for i in list(map(str,[self.yfirst,self.ywin,self.outhand(self.yhand),self.outhand(self.chand),self.yez,self.cez])):
            l += "," + i
        with open(outfile,"a",encoding = "utf-8") as fo:
            fo.write(l)
            for j in self.turns:
                fo.write(" "+j.output())
            fo.write("\n")
    
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

def ezcal(ez):
    global eznum
    if ez == 1:return "0枚"
    elif ez <= 6:return "1枚("+["T","J","Q","K","X"][ez-2]+")"
    elif ez <= 21:return "2枚("+eznum[0][ez-7]+")"
    elif ez <= 55:return "3枚("+eznum[1][ez-22]+")"
    elif ez <= 120:return "4枚("+eznum[2][ez-56]+")"
    elif ez <= 227:return "5枚("+eznum[3][ez-121]+")"
    elif ez <= 234:return "6枚(JKX"+str(ez-228)+"枚)"
    elif ez <= 239:return str(ez-235)+"枚"
    else:return "E"

def substituteh(st):
    st = st.replace("+","")
    st = st.replace("10","T")
    st = st.replace("11","J")
    st = st.replace("12","Q")
    st = st.replace("13","K")
    st = st.replace("★","X")
    return st
    
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
    st = st.replace("-","%")
    return st

def readnturn(yturn,n):
    n = substitute(n)
    if n == "lose":
        print("エラーです。コードrnt11")
        ret = turn(yturn)
        return ret
    if n == "%":
        ret = turn(yturn,pas = 1)
        return ret
    i = 0
    nlen = len(n)
    draw = 0
    if n[0] != "[":
        draw = n[0]
        i += 2
        try:
            if n[2] == "%":
                ret = turn(yturn,draw = draw,pas = 1)
                return ret
        except IndexError:
            ret = turn(yturn,pas = 1)
            return ret
    if n[i] != "[":
        print("エラーです。コードrnt12")
        ret = turn(yturn)
        return ret
    beg = i+1
    end = n.find("]")
    p = n[beg:end].split(sep = ",")
    i = end+2
    if i >= nlen:
        ret = turn(yturn,draw = draw,p = p)
        return ret
    pfac = 0
    if n[i] == ",":
        i += 1
    if n[i] == "[":
        beg = i+1
        end = beg + n[beg:].find("]")
        pfac = n[beg:end].split(sep = ",")
        i = end + 2
    else:
        if n[i] == ",":
            i += 1
    if i >= nlen:
        ret = turn(yturn,draw = draw,p = p,pfac = pfac)
        return ret
    penalty = n[i:-2].split(sep=",")
    ret = turn(yturn,draw = draw,p = p,pfac = pfac,bad = 1,penalty = penalty,pas = 1)
    return ret

def readnirecord():
    global games
    while True:
        print('入力は３つあります。1/3\n'+
              'nishimuraさんの形式になっている棋譜を、後から読み込みやすいVCR形式に変換します。\n'+
              '読み込むＣＰＵ対戦の記録テキストファイルを、\n'+
              'このプログラムファイルと同じ場所に保存してください。\n'+
              '読み込むファイルの名前を、.txtを含めず入力してください。')
        foname = input()+".txt"
        print("2/3")
        print('変換したVCRデータを保存するファイルの名前を、.txtなしで入力してください。\n'+
              '既存のファイル名を入力した場合、元のデータを保持したままデータを追加します。')
        fwname = input()+".txt"
        print("3/3")
        print(foname+'を開き、データを変換して'+fwname+'に保存します。元のデータは保持されます。\n'+
              '間の"--------"は削除せず、空行を入れないでください。\n'+
              '準備ができたら1を、訂正する場合はbackを、ホームに戻る場合はhomeを入力してください。')
        inp=input()
        if inp == "home":
            return
        elif inp == "1" or inp == "１":
            break
        try:
            with open(fwname,"r",encoding = "utf-8") as fw:
                if "vcr" != fw.readline():
                    print("書き込むファイルはvcr形式ではありません。それでも続けますか？\n"+
                          "はい：１　いいえ：０")
                    try:
                        if int(input()) != 1:
                            continue
                    except ValueError:
                        continue
        except FileNotFoundError:
            with open(fwname,"w",encoding = "utf-8") as fw:
                fw.write("vcr\n")
    print("読み込みを開始します。この処理は時間がかかる事があります。")
    with open(foname,"r",encoding = "utf-8") as f:
        con = True
        while con:
            turns = []
            try:
                yfirst,l=f.readline().split(sep = ":")
            except ValueError:
                break
            
            try:
                d,m = f.readline().split(sep=":")
            except ValueError:
                print("エラーが発生しました。コード:rn12")
                break
            if yfirst == "you":
                yfirst = 1
            else:
                yfirst = 0
            yhand = substituteh([m,l][yfirst]).split(sep=",")
            chand = substituteh([l,m][yfirst]).split(sep=",")
            del d,l,m
            while True:
                try:
                    yturn,n = f.readline().split(sep=":")
                except ValueError:
                    con = False
                    print("エラーが発生しました。コード:rn21")
                    break
                if yturn == "you":
                    yturn = 1
                else:
                    yturn = 0
                if "lose" in n:
                    ylose = yturn
                    f.readline()
                    break
                else:
                    nturn = readnturn(yturn,n)
                    turns.append(nturn)
            new = game(len(turns),turns,yfirst,int(not ylose),yhand,chand)
            games.append(new)
            new.output(fwname)
    print("読み込みが完了しました。")
    print("続けて読み込んだデータを分析しますか？はい：１　いいえ：０")
    if input() in ["1","１"]:
        analysevcr(fwname)
    
def analysevcr(fname = 0):
    global games
    if not fname:
        del games
        games = []
        while True:
            print("VCR形式のファイルを読み込み、分析します。\n"+
                  "読み込むファイルの名前を、.txtを含めず入力してください。終了：end")
            fname = input() + ".txt"
            if fname == "end.txt":
                print("ホームに戻ります。\n")
                return
            print(fname + "を開きます。よろしいですか？はい：１　いいえ：０　終了：end")
            inp = input()
            if inp in ["1","１"]:
                break
            if inp == "end":
                print("ホームに戻ります。\n")
                return
        with open(fname,"r",encoding = "utf-8") as f:
            for line in f:
                gandt = line.split(sep=" ")
                turnlen,yfirst,ywin,yhand,chand,yez,cez = gandt[0].split(sep = ",")
                turns = []
                for i in gandt[1:]:
                    yourturn,draw,p,pfac,bad,penalty,pas = i.split(sep = ",")
                    newturn = turn(int(yourturn),draw,p,pfac,int(bad),penalty,int(pas))
                    turns.append(newturn)
                newgame = game(int(turnlen),turns,int(yfirst),int(ywin),yhand,chand,int(yez),int(cez))
                games.append(newgame)
    while True:
        print("統計を出します。テキストファイルとして出力します。\n"+
              "出力するテキストファイルのファイル名を.txtを含めずに入力してください。")
        foname = input() + ".txt"
        print(foname + "に出力します。よろしいですか？はい：１　いいえ：０ 終了：end")
        inp = input()
        if inp == "end":
            print("ホームに戻ります。\n")
            return
        elif inp in ["1","１"]:
            break
    while True:
        print("出力したいデータのコードを入力してください。\n"+
              "終了：end 基本情報:0 革命・57カットの回数:1\n"+
              "先手の初手の枚数:2\n"+
              "絵札分類の相関のcsvファイル:3")
        mode = input()
        if mode == "end":
            print("ホームに戻ります。\n")
            return
        try:
            mode=int(mode)
        except ValueError:
            print("正しい値を入力してください。")
        with open(foname,"a") as fo:
            if mode == 0:
                gamenum = len(games)
                fo.write("試合数："+str(gamenum)+"\n")
                winnum = 0
                winfirst = 0
                firstnum = 0
                for i in games:
                    winnum += i.ywin
                    if i.yfirst:
                        winfirst += i.ywin
                        firstnum += 1
                try:
                    fo.write("プレーヤーの勝利数/勝率:"+str(winnum)+"/{:.2%}\n".format(winnum/gamenum))
                    fo.write("プレーヤーの先攻時の勝利数/勝率:"+str(winfirst)+"/{:.2%}\n".format(winfirst/firstnum))
                    fo.write("プレーヤーの後攻時の勝利数/勝率:"+str(winnum-winfirst)+"/{:.2%}\n".format((winnum-winfirst)/(gamenum-firstnum)))
                except ZeroDivisionError:
                    print("試合数が不足しているため、正しく記録されませんでした。")
                print("基本情報の書き込みが終了しました。")
            elif mode == 1:
                gamenum,gc,gcend,gcendg,gcg,rl,rlg = len(games),0,0,0,0,0,0
                for i in games:
                    orgcg,orrlg = 0,0
                    for j in range(i.turnlen):
                        if i.turns[j].pfac == "0":
                            turnp = i.turns[j].p.replace("X","")
                            if turnp == "57":
                                gc += 1
                                if not orgcg:
                                    orgcg = 1
                                    gcg += 1
                                if j == i.turnlen-3:
                                    if not gcendg:
                                        gcend += 1
                                        gcendg = 1
                            elif turnp == "1729":
                                rl += 1
                                if not orrlg:
                                    orrlg += 1
                                    rlg += 1
                try:
                    fo.write("グロタンカットの回数:"+str(gc)+"\n")
                    fo.write("グロタンカットのあった試合の数/割合:"+str(gcg)+"/{:.2%}\n".format(gcg/gamenum))
                    fo.write("グロタンカットから上がった回数/割合:"+str(gcend)+"/{:.2%}\n".format(gcend/gamenum))
                    fo.write("ラマヌジャン革命の回数:"+str(rl)+"\n")
                    fo.write("ラマヌジャン革命のあった試合の数/割合:"+str(rlg)+"/{:.2%}\n".format(rlg/gamenum))
                except ZeroDivisionError:
                    print("試合数が不足しているため、正しく記録されませんでした。")
                print("革命・57カットの回数の書き込みが終了しました。")
            elif mode == 2:
                fpmany = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                for i in games:
                    fp = i.turns[0].p.replace("X","")
                    if i.turns[0].pas:
                        fpmany[0] += 1
                    else:
                        fpmany[len(fp)] += 1
                fo.write("先手の初手枚数\nパスまたは素数でない数を出した回数:"+str(fpmany[0])+"\n")
                for i in range(1,13):
                    fo.write(str(i)+"枚出し:"+str(fpmany[i])+"\n")
                print("先手の初手枚数の書き込みが完了しました。")
            elif mode == 3:
                back = False
                while True:
                    while True:
                        print("出力するcsvファイルのファイル名を.csvを含めずに入力してください。\n"+
                              "注意:必ず新しいファイル名を入力してください。新規作成する必要はありません。")
                        fwname = input()+".csv"
                        print(fwname+"に出力します。よろしいですか？はい：１　いいえ：０ 終了：end")
                        inp = input()
                        if inp in ["1","１"]:
                            break
                        elif inp == "end":
                            back = True
                            break
                    if back:
                        break
                    try:
                        with open(fwname,"w"):
                            pass
                    except PermissionError:
                        print(fname,"が存在します。該当ファイルを削除するか、ファイル名を変更してください。\n")
                        continue
                    print("出力します。\nこの処理には時間がかかることがあります。\n")
                    a = [["絵札属性番号","絵札属性","試合数","勝","敗","グロタン勝","グロタン敗","革命勝","革命敗","パス勝","パス敗","1枚勝","1枚敗","2枚勝","2枚敗","3枚勝","3枚敗","4枚勝","4枚敗","5枚勝","5枚敗","6枚以上勝","6枚以上敗","勝・相手絵札属性番号","敗・相手絵札属性番号"]]
                    for i in range(1,240):
                        a.append([i,ezcal(i),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,[],[]])
                    for g in games:
                        rl = 0
                        if g.turns[0].p == 0:
                            fpmany = 0
                        else:
                            fpmany = len(g.turns[0].p.replace("X",""))
                        gcend = g.turns[-3].p.replace("X","") == "57" and g.turns[-3].pfac == "0"
                        for j in g.turns:
                            if j.pfac == "0":
                                if j.p.replace("X","") == "1729":
                                    rl = 1
                        a[g.yez][2] += 1
                        a[g.yez][4-g.ywin] += 1
                        a[g.yez][24-g.ywin].append(cez)
                        a[g.yez][10+2*fpmany-g.ywin]
                        if gcend:
                            a[g.yez][6-g.ywin] += 1
                        if rl:
                            a[g.yez][8-g.ywin] += 1
                    b = ["計","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"",""]
                    for c in a[1:]:
                        for i in range(2,22):
                            b[i] += c[i]
                        o,p = "",""
                        for d in c[23]:
                            o += str(d)
                        for d in c[24]:
                            p += str(d)
                        c[23],c[24] = o,p
                    a.append(b)
                    for r in range(len(a)):
                        for s in range(len(a[r])):
                            if a[r][s] == 0:
                                a[r][s] = ""
                    with open(fwname,"w+") as fw:
                        w = csv.writer(fw,lineterminator="\n")
                        w.writerows(a)
                    print("ファイルの作成が完了しました。\n"+
                          "エクセルからこのファイルを開く場合、\n"+
                          "ファイル>開く　より作製したcsvファイルを選択してください。\n")
                if back:
                    continue
            else:
                print("正しい値を入力してください。")

def home():
    while True:
        print("VsCpuRecorder ホームです。行いたい操作のコードを入力してください。\n"+
              'nishimuraさんの形式になっているデータを、VCR形式に変換する：ntov\n'+
              'VCR形式のデータを分析する：datas 終了：end')
        inp = input()
        if inp == "end":
            print("終了します。")
            input("終了するにはエンターを押してください...")
            return
        elif inp == "ntov":
            readnirecord()
        elif inp == "datas":
            analysevcr()
            
if "__main__" == __name__ :
    home()