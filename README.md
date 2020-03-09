# 勾配法：反復による最小値探索
## 学習率0.01（収束）
![gd01](/gradient_descent_01.gif)
## 0.01（谷の反対側の初期値から収束）
![gd01a](/gradient_descent_01a.gif)
## 0.04（速い収束）
![gd04](/gradient_descent_04.gif)
## 0.06（発散）
![gd06](/gradient_descent_06.gif)

# matplotlibでグラフ作成
## 準備
### パッケージのダウンロード・インストール
```
pip install pandas
pip install matplotlib
```
---
### matplotlibで日本語を表示するためのフォント追加・設定
- IPAexフォントをダウンロード
- https://ipafont.ipa.go.jp/node26#jp
- IPAexゴシック(Ver.003.01)
- ipaexg00301.zip(3.92MB)
```
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
---------
matplotlib.matplotlib_fname()
のフォルダの
matplotlibrcファイルを
matplotlib.get_configdir()
のフォルダにコピーして編集
#font.family         : sans-serif
font.family:IPAexGothic
の１行を追加

または

matplotlibrcの代わりに，
plt.rcParams['font.family'] = 'IPAexGothic'
をコードに入れる
以下に掲載したプログラムはこの方法
```
---
## グラフ作成の流れ
1. データの準備・前処理
2. X軸、Y軸のデータを決める
3. グラフの種類を決める
4. グラフの飾りを付ける
5. 表示・保存
---
## データ
- [家計簿.csv](/家計簿.csv)
## 例題1
- [kakeibo1.py](/kakeibo1.py)
- ![fig1](/家計簿_fig1.png)
- ![fig1a](/家計簿_fig1a.png)
## 例題2
- [kakeibo2.py](/kakeibo2.py)
- ![fig2](/家計簿_fig2.png)
## 例題3
- [kakeibo3.py](/kakeibo3.py)
- ![fig3](/家計簿_fig3.png)
## 練習1
- [kakeibo4.py]
- ![fig4](/家計簿_fig4.png)
## 練習2
- [kakeibo5.py](/kakeibo5.py)
- ![fig5](/家計簿_fig5.png)
- ![fig5a](/家計簿_fig5a.png)
## 練習3
- [kakeibo6.py]
- ![fig6](/家計簿_fig6.png)
