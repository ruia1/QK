# -*- coding: utf-8 -*-
#各モードを開くためのプログラム

import goropri,primalytest,gamemode,psearch,panalyze

def qkhelp():
    #"試合モード:試合進行を、素数判定や記録でサポートします。\n"+
    print("素数判定　:素数判定をします。\n"+
          "素数探索　:素数を様々な条件で探索できます。\n"+
          "語呂モード:語呂素数の探索をします。\n")
          #"分析モード:試合モードで記録したデータや、CPU対戦")#分析モード準備中
    
def qkhome():
    while True:
        print("QK Supporter ホームです。すすみたいモードのコードを入力してください。\n"+
              "素数判定:ptest 素数探索:search 語呂モード:goro\n"+
              "ヘルプ:help 終了:end")
              #"分析モード:analyze ヘルプ:help 終了:end")
        modes = input()
        print()
        if modes == "end":
            print("終了します。")
            input("終了するにはエンターを押してください...")
            return
        elif modes == "ptest":#素数判定モード
            primalytest.pthome()
        #elif modes == "game":#試合モード
        #    gamemode.gmhome()
        elif modes == "search":#素数探索
            psearch.sehome()
        elif modes == "goro":#語呂モード
            goropri.gohome()
        #elif modes == "analyze":#分析モード
        #    panalyze.anhome()
        elif modes == "help":
            qkhelp()
        else:
            print("正しい値を入力してください。")