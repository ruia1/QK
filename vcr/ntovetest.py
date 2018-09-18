# -*- coding: utf-8 -*-
import sys, codecs
sys.stdout = codecs.getwriter("shift_jis")
with codecs.open("ni.txt","r",'shift_jis') as f:
    for line in f:
        with open("test.txt","w") as g:
            g.write(line)
#yfirst,l = u(f.readline(),"utf-8").encode("utf-8").split(sep=":")
        #except ValueError:
            #print("エラーが発生しました。コード:rn11")
"""            
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
"""