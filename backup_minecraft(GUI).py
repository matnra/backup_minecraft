import tkinter
from tkinter import messagebox
from tkinter import font
import shutil
import datetime
import os


#click時のイベント
def btn_click():
    #'C:\\Users\\sm\\AppData\\Roaming\\.minecraft\\saves'ディレクトリの中身をコピー、,'E:\\マイクラセーブデータ\\XXXXXXXX'に、ディレクトリ名を付けて中身を保存
    shutil.copytree('C:\\Users\\sm\\AppData\\Roaming\\.minecraft\\saves','E:\\マイクラセーブデータ\\XXXXXXXX')

    #カレントディレクトリを"E:\\マイクラセーブデータ"に変更
    os.chdir("E:\\マイクラセーブデータ")

    #現在日時のdatetimeオブジェクトを取得し、now変数に入れる
    now=datetime.datetime.now()

    #変更したい名前("XXXXXXXX")をold変数に入れる
    old="XXXXXXXX"

    #formatメソッドを使用して、日付を取得し、"{0:%Y%m%d}"の書式にする、それをnew変数に入れる
    new="{0:%Y%m%d}".format(now)

    #os.rename(変更前ファイル、変更後ファイル)
    os.rename(old,new)
    
    #バックアップ終了メッセージ
    messagebox.showinfo("バックアップ終了","バックアップが終了しました")
    tki.destroy()

    
    
#画面作成
tki = tkinter.Tk()
tki.geometry('300x200')#画面サイズの設定
tki.title('マインクラフトバックアップ')#画面タイトルの設定

#ラベル作成
label = tkinter.Label(tki,text="本日分のマインクラフトのバックアップを取りますか？")
label.place(x=30,y=30)

#ボタンの作成
btn = tkinter.Button(tki,text='開始',height = 5, width = 36,command = btn_click)#ボタンの設定(text=ボタンに表示するテキスト)
btn.place(x=20,y=70)#ボタンを配置する位置の設定


#画面をそのまま表示
tki.mainloop()