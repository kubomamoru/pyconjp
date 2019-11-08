import pandas as pd
import matplotlib.pyplot as plt

Z = pd.read_csv('家計簿.csv')

Z_sum = Z.groupby('分類', as_index=False).sum()

Z_sum_sorted = Z_sum.sort_values('支出', ascending=False)

plt.rcParams['font.family'] = 'IPAexGothic'

fig, ax = plt.subplots(1,3, figsize=(15,5))
#3個サブプロット作成（1列に3個）、全体の幅・高さのサイズ（インチ単位）

X = Z_sum_sorted['分類']
Y = Z_sum_sorted['支出']

# color palettes for Tableau 10
# ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', C6', 'C7', 'C8', C9'] 
color_list = ['C{}'.format(i) for i in range(len(X))]

axx = ax[0]
axx.bar(X, Y, color=color_list)
axx.grid(linestyle='--')
axx.set_title('棒グラフ')

axx = ax[1]
axx.barh(X, Y, color=color_list)
axx.xaxis.tick_top()
axx.invert_yaxis()
axx.grid(linestyle='--')
axx.set_title('横向き棒ブラフ') #上部のタイトル

axx = ax[2]
axx.pie(Y, labels=X,
        autopct='%.2f%%',
        startangle=90,
        counterclock=False,
        textprops={'size': 'smaller'})
axx.set_title('円グラフ') #上部のタイトル
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
fig.subplots_adjust(left=0.1, top=0.8, wspace=0.3) #周りの余白の調整
fig.suptitle('家計簿（練習2）')
fig.set(facecolor='#eeeeee') #背景色facecolor
fig.savefig('家計簿_fig5a.png')
fig.show()

ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=30, ha='right')
