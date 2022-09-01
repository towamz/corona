from tkinter import *
from tkinter import ttk
import tkinter


def execProc():
    targetPref = []
    
    regionCnt=-1
    
    for i in chk_txt:
        regionCnt += 1
        cnt=-1
        for j in i:
            cnt += 1
        
            #print(chk_txt[regionCnt][cnt],chk_bln[chk_txt[regionCnt][cnt]].get())
            if chk_bln[chk_txt[regionCnt][cnt]].get():
                targetPref.append(chk_txt[regionCnt][cnt])
    
    print(targetPref)
    #print("終わり")
    






root = Tk()
root.title('コロナ陽性者数グラフ化サンプルコード')

# Frame
frame1 = ttk.Frame(root, padding=(50))
frame1.grid()



# チェックボタンのラベルをリスト化する
# 地域別に2重リストにしている
chk_txt = [
            ['Hokkaido','Aomori','Iwate','Miyagi','Akita','Yamagata','Fukushima'],
            ['Ibaraki','Tochigi','Gunma','Saitama','Chiba','Tokyo','Kanagawa'],
            ['Niigata','Yamanashi','Nagano'],
            ['Gifu','Shizuoka','Aichi','Mie'],
            ['Toyama','Ishikawa','Fukui'],
            ['Shiga','Kyoto','Osaka','Hyogo','Nara','Wakayama'],
            ['Tottori','Shimane','Okayama','Hiroshima','Yamaguchi'],
            ['Tokushima','Ehime','Kochi','Kagawa'],
            ['Fukuoka','Saga','Nagasaki','Kumamoto','Oita','Miyazaki','Kagoshima','Okinawa']           
        ]

# チェックボックスの状態を保存する変数
chk_bln = {}


# チェックボタンを動的に作成して配置
regionCnt=0
cnt = 0

for i in chk_txt:
    regionCnt += 1
    cnt=0
    for j in i:
        cnt += 1
       
        print(j[0])

        chk_bln[j] = BooleanVar()
        
        chk = Checkbutton(frame1, variable=chk_bln[j], text=j, onvalue=True, offvalue=False) 
        chk.grid(row=regionCnt, column=cnt, sticky=W)



# グラフ化実行ボタン
button1 = tkinter.Button(frame1, text='グラフ化', command=execProc)
button1.grid(row=10, column=0, columnspan=3)

Label(root, text ='表示する都道府県を選択してください').place(x = 0, y = 0)
Label.pack(frame1)

root.mainloop()