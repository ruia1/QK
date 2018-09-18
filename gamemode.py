# -*- coding: utf-8 -*-
import primalytest

class setting:
    def __init__(self,plc,pl,):
        self.plc = plc
        self.pl = pl
def gmhome():
    print("試合モードです。\n")
    while True:
        print("試合の人数を入力してください。")
        peoplec = input()
        print()
        if peoplec == "end":
            print("終了します。")
            if __name__ == '__main__':
                input("終了するにはエンターを押してください...")
            return
        try:
            peoplec = int(peoplec)
            break
        except ValueError:
            print("正しい値を入力してください。")
    print("名前を入力しますか？　はい：１ いいえ：０ を入力してください。")
    orn = input()
    if orn == "1" or orn == "１":
        orn = True
        while True:
            people = []
            for i in range(peoplec):
                pl = ""
                if pl == 1:
                    people.append("プレイヤー"+str(i))
                print("プレイヤー"+str(i)+"の名前を入力してください。\n"+
                      "入力しない場合は、そのプレイヤー以降「プレイヤー"+str(i)+"」で登録されます。")
                pl = input()
                print()
                if pl == "":
                    pl = 1
                    people.append("プレイヤー"+str(i))
                else:
                    people.append(pl)
        for j in range(peoplec):
            print("プレイヤー"+str(i)+":"+people[j])
        print("で登録します。よろしいですか？　はい：１ いいえ：０ を入力してください。")
        okn = input()
        print()
        
        