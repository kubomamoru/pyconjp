import pandas as pd
import matplotlib.pyplot as plt

Z = pd.read_csv('家計簿.csv')

# '分類'列の値ごとにグループ化してsum()で集計
# as_index=False：行番号を付ける指定、この指定が無いと行番号の代わりにグループ名になる
Z_sum = Z.groupby('分類', as_index=False).sum()

# '支出'列の値で降順に並べる、昇順はascending=True
Z_sum_sorted = Z_sum.sort_values('支出', ascending=False)

plt.rcParams['font.family'] = 'IPAexGothic'
fig, ax = plt.subplots()

X = Z_sum_sorted['分類'] #groupbyでグループ化した'分類'列
Y = Z_sum_sorted['支出'] #集計した'支出'列

ax.pie(Y, labels=X,       #円グラフの大きさとそのラベル
        autopct='%.2f%%', #割合%を少数2桁で表示
        startangle=90,    #x軸から時計回りに90度から始める
        counterclock=False,#時計回り、通常は反時計回り
        textprops={'size': 'smaller'}) #色の指定無し

fig.suptitle('家計簿（分類ごと集計、支出降順）')
fig.set(facecolor='#eeeeee') #背景色facecolor
fig.savefig('家計簿_fig3.png')
fig.show()
