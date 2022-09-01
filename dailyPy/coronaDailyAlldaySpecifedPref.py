from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


def execProc():
    targetPref = []
    
    for regionList in chk_txt:
        for currentPref in regionList:
            
            if chk_bln[currentPref].get():
                targetPref.append(currentPref)
        
    
    #オープンデータ(csv)を読み込み、グラフ表示する
    df = pd.read_csv("C:\sampleMacro\\2201コロナ\\newly_confirmed_cases_daily.csv", index_col=0)
    pd.set_option('display.unicode.east_asian_width', True)
    
    #グラフ化して表示する
    df[targetPref].plot()
    plt.show()







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
for regionCnt, regionList in enumerate(chk_txt):
    for cnt, currentPref in enumerate(regionList):

        chk_bln[currentPref] = BooleanVar()
        
        chk = Checkbutton(frame1, variable=chk_bln[currentPref], text=currentPref, onvalue=True, offvalue=False) 
        chk.grid(row=regionCnt, column=cnt, sticky=W)



# グラフ化実行ボタン
button1 = ttk.Button(frame1, text='グラフ化', command=execProc)
button1.grid(row=10, column=0, columnspan=3)

Label(root, text ='表示する都道府県を選択してください').place(x = 0, y = 0)
Label.pack(frame1)

root.mainloop()