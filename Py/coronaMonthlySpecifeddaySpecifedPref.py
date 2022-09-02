from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from tkcalendar import DateEntry 



def execProc():
    targetPref = []
    
    for regionList in chk_txt:
        for currentPref in regionList:
            
            if chk_bln[currentPref].get():
                targetPref.append(currentPref)
    
    

    #オープンデータ(csv)を読み込み、グラフ表示する
    #インデックスを抽出条件にする方法が見つからなかったので、dateを通常の列として読み込み後でインデックスに設定する
    #df = pd.read_csv("C:\sampleMacro\\2201コロナ\\newly_confirmed_cases_daily.csv", index_col=0, parse_dates=True)
    df = pd.read_csv("C:\sampleMacro\\2201コロナ\\newly_confirmed_cases_daily.csv")
    pd.set_option('display.unicode.east_asian_width', True)

    df["Date"]=pd.to_datetime(df["Date"])
    df = df[(df["Date"] >= pd.to_datetime(dateStart.get_date())) & (df["Date"] <= pd.to_datetime(dateEnd.get_date()))]
    df = df.set_index("Date")
    df = df.resample("MS").sum()
    df = df[targetPref]    
    
    #グラフ化して表示する
    df.plot()
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




#開始・終了日を取得
dateStartLabel = Label(frame1, text="開始日")
dateStartLabel.grid(row=10,column=0, sticky=E)
dateStart=DateEntry(frame1,selectmode='day', date_pattern='yyyy-mm-dd',year=2020,month=1,day=16)
dateStart.grid(row=10,column=1)


dateEndLabel = Label(frame1, text="終了日")
dateEndLabel.grid(row=10,column=2, sticky=E)
dateEnd=DateEntry(frame1,selectmode='day', date_pattern='yyyy-mm-dd')
dateEnd.grid(row=10,column=3)




# グラフ化実行ボタン
button1 = ttk.Button(frame1, text='グラフ化', command=execProc)
button1.grid(row=11, column=0)

Label(root, text ='表示する都道府県を選択してください').place(x = 0, y = 0)
Label.pack(frame1)

root.mainloop()