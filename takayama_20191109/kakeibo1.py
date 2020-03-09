import pandas as pd
import matplotlib.pyplot as plt
# for MacOS
# import matplotlib
# matplotlib.use('TkAgg')

Z = pd.read_csv('家計簿.csv')
# 列名
# '年月日'
# '曜日'
# '費目'
# '分類'
# '支出'

# グラフに日本語を表示するためのゴシックフォント設定
plt.rcParams['font.family'] = 'IPAexGothic'

# グラフの領域全体, グラフの描画領域
fig, ax = plt.subplots()

# X軸のデータと、Y軸のデータ
X = Z['年月日'] # '年月日'列
Y = Z['支出']   # '支出'列

# グラフの種類
ax.barh(X, Y) #横向き棒グラフ（Y軸=X、X軸=Yに入れ替わる）

#　グラフの飾り
ax.xaxis.tick_top() #x軸のメモリを上に付ける、通常は下
ax.invert_yaxis()   #y軸を逆に上から下にする、通常は下から上
ax.grid(linestyle='--') #格子を破線で描く

# 全体の飾り
fig.suptitle('家計簿') #上部のタイトル
fig.subplots_adjust(left=0.2) #サブプロットの調整：Y軸のラベルがはみ出ないように左スペースを少し広げる
#left=0.125, right=0.9, bottom=0.1, top=0.9
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
fig.set(facecolor='#eeeeee') #背景色facecolor、白#ffffff、値が小さいほど暗い

# 画像保存、表示
fig.savefig('家計簿_fig1.png')
fig.show() #これが無いと、表示されない

'''
日本語フォント
IPAexフォントをダウンロード
https://ipafont.ipa.go.jp/node26#jp
IPAexゴシック(Ver.003.01)
ipaexg00301.zip(3.92MB)

import matplotlib
matplotlib.matplotlib_fname()
で表示されたフォルダ内の
fonts/ttf/
にipaexg00301.zipの中の
ipaexg.ttf
をコピー

matplotlib.get_configdir()
のフォルダ内のキャッシュファイル
fontList.cache
fontList.py3k.cache
fontList.json
削除

matplotlib.matplotlib_fname()
で表示されたフォルダの
matplotlibrcをコピーして編集
#font.family         : sans-serif
font.family:IPAexGothic

または

matplotlibrcの代わりに，
plt.rcParams['font.family'] = 'IPAexGothic'
'''
