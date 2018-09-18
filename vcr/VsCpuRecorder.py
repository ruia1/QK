# -*- coding: utf-8 -*-ｓ

games = []

class game:
    def __init__(self,turnlen,turns,yfirst,ylose,yhand,chand,ytjqkx=0,ctjqkx=0):
        self.turnlen = turnlen
        self.turns = turns
        self.yfirst = yfirst
        self.yhand = yhand.sort()
        self.chand = chand.sort()
        self.ywin = int(not ylose)
        self.ytjqkx = ytjqkx
        self.ctjqkx = ctjqkx
    
    def settjqkx(self):
        self.ytjqkx = self.caltjqkx("y",self.yhand)
        self.ctjqkx = self.caltjqkx("c",self.chand)
        
    def caltjqkx(self,hand):
        tjlis = [hand.count("T"),hand.count("J"),
                 hand.count("Q"),hand.count("K"),hand.count("X")]
        ycount = sum(tjlis)
        if ycount >= 7:
            return ycount+228
        elif ycount == 6:
            return tjlis[1]+tjlis[3]+tjlis[4]+228
        elif ycount == 0:
            return 1
        elif ycount == 1:
            for i in range(5):
                if tjlis[i] == 1:
                    return i+2
        else:
            tjstr = ""
            for i in range(5):
                tjstr += tjlis[i] * ["T","J","Q","K","X"][i] 
            if ycount == 2:
                l = ['TT', 'TJ', 'TQ', 'TK', 'TX', 'JJ', 'JQ', 'JK', 'JX', 'QQ', 'QK', 'QX', 'KK', 'KX', 'XX']
                return 7 + l.index(tjstr)
            elif ycount == 3:
                l = ['TTT', 'TTJ', 'TTQ', 'TTK', 'TTX', 'TJJ', 'TJQ', 'TJK', 'TJX', 'TQQ', 'TQK', 'TQX', 'TKK', 'TKX', 'TXX', 'JJJ', 'JJQ', 'JJK', 'JJX', 'JQQ', 'JQK', 'JQX', 'JKK', 'JKX', 'JXX', 'QQQ', 'QQK', 'QQX', 'QKK', 'QKX', 'QXX', 'KKK', 'KKX', 'KXX']
                return 22 + l.index(tjstr)
            elif ycount == 4:
                l = ['TTTT', 'TTTJ', 'TTTQ', 'TTTK', 'TTTX', 'TTJJ', 'TTJQ', 'TTJK', 'TTJX', 'TTQQ', 'TTQK', 'TTQX', 'TTKK', 'TTKX', 'TTXX', 'TJJJ', 'TJJQ', 'TJJK', 'TJJX', 'TJQQ', 'TJQK', 'TJQX', 'TJKK', 'TJKX', 'TJXX', 'TQQQ', 'TQQK', 'TQQX', 'TQKK', 'TQKX', 'TQXX', 'TKKK', 'TKKX', 'TKXX', 'JJJJ', 'JJJQ', 'JJJK', 'JJJX', 'JJQQ', 'JJQK', 'JJQX', 'JJKK', 'JJKX', 'JJXX', 'JQQQ', 'JQQK', 'JQQX', 'JQKK', 'JQKX', 'JQXX', 'JKKK', 'JKKX', 'JKXX', 'QQQQ', 'QQQK', 'QQQX', 'QQKK', 'QQKX', 'QQXX', 'QKKK', 'QKKX', 'QKXX', 'KKKK', 'KKKX', 'KKXX']
                return 56 + l.index(tjstr)
            else:
                l = ['TTTTJ', 'TTTTQ', 'TTTTK', 'TTTTX', 'TTTJJ', 'TTTJQ', 'TTTJK', 'TTTJX', 'TTTQQ', 'TTTQK', 'TTTQX', 'TTTKK', 'TTTKX', 'TTTXX', 'TTJJJ', 'TTJJQ', 'TTJJK', 'TTJJX', 'TTJQQ', 'TTJQK', 'TTJQX', 'TTJKK', 'TTJKX', 'TTJXX', 'TTQQQ', 'TTQQK', 'TTQQX', 'TTQKK', 'TTQKX', 'TTQXX', 'TTKKK', 'TTKKX', 'TTKXX', 'TJJJJ', 'TJJJQ', 'TJJJK', 'TJJJX', 'TJJQQ', 'TJJQK', 'TJJQX', 'TJJKK', 'TJJKX', 'TJJXX', 'TJQQQ', 'TJQQK', 'TJQQX', 'TJQKK', 'TJQKX', 'TJQXX', 'TJKKK', 'TJKKX', 'TJKXX', 'TQQQQ', 'TQQQK', 'TQQQX', 'TQQKK', 'TQQKX', 'TQQXX', 'TQKKK', 'TQKKX', 'TQKXX', 'TKKKK', 'TKKKX', 'TKKXX', 'JJJJQ', 'JJJJK', 'JJJJX', 'JJJQQ', 'JJJQK', 'JJJQX', 'JJJKK', 'JJJKX', 'JJJXX', 'JJQQQ', 'JJQQK', 'JJQQX', 'JJQKK', 'JJQKX', 'JJQXX', 'JJKKK', 'JJKKX', 'JJKXX', 'JQQQQ', 'JQQQK', 'JQQQX', 'JQQKK', 'JQQKX', 'JQQXX', 'JQKKK', 'JQKKX', 'JQKXX', 'JKKKK', 'JKKKX', 'JKKXX', 'QQQQK', 'QQQQX', 'QQQKK', 'QQQKX', 'QQQXX', 'QQKKK', 'QQKKX', 'QQKXX', 'QKKKK', 'QKKKX', 'QKKXX', 'KKKKX', 'KKKXX']
                return 121 + l.index(tjstr)
            
    def output(self,outfile):
        l = str(self.turnlen)
        for i in list(map(str,[self.yfirst,self.ywin,self.yhand,self.chand,self.ytjqkx,self.ctjqkx])):
            l += "," + i
        with open(outfile,"a") as fo:
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
    print(n)
    if "%" in n:
        ret = turn(yturn,pas = 1)
        return ret
    i = 0
    nlen = len(n)
    draw = 0
    if n[0] != "[":
        draw = n[0]
        i += 2
        print(n)
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
            with open(fwname,"r") as fw:
                if "vcr" != fw.readline():
                    print("書き込むファイルはvcr形式ではありません。それでも続けますか？\n"+
                          "はい：１　いいえ：０")
                    try:
                        if int(input()) != 1:
                            continue
                    except ValueError:
                        continue
        except FileNotFoundError:
            with open(fwname,"w") as fw:
                fw.write("vcr\n")
    print("読み込みを開始します。この処理は時間がかかる事があります。")
    with open(foname,"r",encoding = "shift_jis") as f:
        con = True
        while con:
            turns = []
            try:
                yfirst,l=f.readline().split(sep = ":")
                #yfirst,l = u(f.readline(),"utf-8").encode("utf-8").split(sep=":")
            except ValueError:
                print("エラーが発生しました。コード:rn11")
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
            new = game(len(turns),turns,yfirst,ylose,yhand,chand)
            games.append(new)
            new.output(fwname)
    print("続けて読み込んだデータを分析しますか？はい：１　いいえ：０")
    try:
        if 1 == int(input()):
            analysevcr()
    except ValueError:
        print("ホームに戻ります。")
    
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
                print("ホームに戻ります。")
                return
            print(fname + "を開きます。よろしいですか？はい：１　いいえ：０　終了：end")
            inp = input()
            if inp == "end":
                print("ホームに戻ります。")
                return
            try:
                if 1 == int(inp):
                    break
            except ValueError:
                pass
        with open(fname,"r") as f:
            for line in f:
                gandt = line.split(sep=" ")
                turnlen,yfirst,ywin,yhand,chand,ytjqkx,ctjqkx = gandt[0].split(sep = ",")
                turns = []
                for i in gandt[1:]:
                    yourturn,draw,p,pfac,bad,penalty,pas = i.split(sep = ",")
                    newturn = turn(int(yourturn),int(draw),p,pfac,int(bad),penalty,int(pas))
                    turns.append(newturn)
                newgame = game(int(turnlen),turns,int(yfirst),int(ywin),yhand,chand,int(ytjqkx),int(ctjqkx))
                games.append(newgame)
    while True:
        print("統計を出します。テキストファイルとして出力します。\n"+
              "出力するテキストファイルのファイル名を.txtを含めずに入力してください。")
        foname = input() + ".txt"
        print(foname + "に出力します。よろしいですか？はい：１　いいえ：０ 終了：end")
        inp = input()
        if inp == "end":
            print("ホームに戻ります。")
            return
        elif inp == "1" or inp == "１":
            break
    while True:
        print("出力したいデータのコードを入力してください。\n"+
              "終了：end 基本情報:0 革命・57カットの回数:1\n"+
              "先手の初手の枚数:2\n"+
              "絵札分類の相関のエクセルシート:3")
        mode = input()
        if mode == "end":
            print("ホームに戻ります。")
            return
        try:
            mode=int(mode)
        except ValueError:
            print("正しい値を入力してください。")
        with open(foname,"a") as fo:
            if mode == 0:
                gamenum = len(games)
                fo.write("試合数："+str(gamenum)+"試合\n")
                winnum = 0
                winfirst = 0
                firstnum = 0
                for i in games:
                    winnum += i.ywin
                    if i.yfirst == 1:
                        winfirst += i.ywin
                        firstnum += 1
                try:
                    fo.write("プレーヤーの勝利数/勝率:"+str(winnum)+"/{:.2%}\n".format(winnum/gamenum))
                    fo.write("プレーヤーの先攻時の勝利数/勝率:"+str(winfirst)+"/{:.2%}\n".format(winfirst/firstnum))
                    fo.write("プレーヤーの後攻時の勝利数/勝率:"+str(winnum-winfirst)+"/{:.2%}\n".format((winnum-winfirst)/(gamenum-firstnum)))
                except ZeroDivisionError:
                    print("試合数が不足しているため、正しく記録されませんでした。")
                print("基本情報の書き込みが終了しました。")
            else:
                print("準備中です。")

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