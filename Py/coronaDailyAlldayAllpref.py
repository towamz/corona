import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSV�t�@�C����ǂݍ���
df = pd.read_csv("C:\sampleMacro\\2201コロナ\\newly_confirmed_cases_daily.csv", index_col=0)
pd.set_option('display.unicode.east_asian_width', True)

#グラフ化して表示する
df.plot()
plt.show()