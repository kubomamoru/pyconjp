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

# color for Tableau 10
# ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', C6', 'C7', 'C8', C9'] 
color_list = ['C{}'.format(i) for i in range(len(X))]

ax.bar(X, Y, color=color_list) #棒グラフ、色の指定

ax.grid(linestyle='--') #格子線

fig.suptitle('家計簿（分類ごと集計、支出降順）')
fig.set(facecolor='#eeeeee') #背景色facecolor
fig.savefig('家計簿_fig2.png')
fig.show()

ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
# x軸のラベル（'分類'列の値）を重ならないように、30度傾ける、右を基準に
# ha:horizontalalignmentの省略形
# fig.show()の後に行う必要がある