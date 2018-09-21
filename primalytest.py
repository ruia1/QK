# -*- coding: utf-8 -*-
#素数判定モード
from milpri import milpri

def ptest(n):
    try:
        m = int(n)
        if m == 57:
            return 57
        elif m == 1729:
            return 1729
        else:
            return milpri(m)
    except ValueError:
        pass
    c = ""
    for i in n:
        if i == "T" or i == "t" or i == "Ｔ" or i == "ｔ":
            c += "10"
        elif i == "J" or i == "j" or i == "Ｊ" or i == "ｊ":
            c += "11"
        elif i == "Q" or i == "q" or i == "Ｑ" or i == "ｑ":
            c += "12"
        elif i == "K" or i == "k" or i == "Ｋ" or i == "ｋ":
            c += "13"
        elif i == "A" or i == "a" or i == "Ａ" or i == "ａ":
            c += "1"
        else:
            c += i
    try:
        ret = int(c)
    except ValueError:
        return "Error"
    return milpri(ret)
        
def pthome():
    orcontinue = "1"
    while orcontinue == "1" or orcontinue == "１":
        print("入力された数を素数判定します。絵札の文字を数字に直す必要はありません。\n"+
              "endで終了します。")
        inp = input("")
        if inp == "end" or inp == "ｅｎｄ":
            print("終了します。")
            if '__main__' == __name__:
                input("終了するには何かキーを押してください...")
            return
        n = ptest(inp)
        if n == "Error":
            print("正しい値を入力してください。")
            continue
        if n == 57:
            print("グロタンディーク素数です。")
        elif n == 1729:
            print("タクシー数です。")
        elif n:
            print("素数です。")
        else:
            print("素数ではありません。")
        orcontinue = input("続けますか？ はい：１ いいえ：０ を入力してください。\n")
        