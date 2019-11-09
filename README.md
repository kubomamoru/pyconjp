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

matplotlib.matplotlib_fname()
で表示されたフォルダの
matplotlibrcをコピーして編集
#font.family         : sans-serif
font.family:IPAexGothic

または

matplotlibrcの代わりに，
plt.rcParams['font.family'] = 'IPAexGothic'
```

---
## 出力例
1. ![fig1](/家計簿_fig1.png)
2. ![fig2](/家計簿_fig2.png)
3. ![fig3](/家計簿_fig3.png)
4. ![fig4](/家計簿_fig4.png)
5. ![fig5](/家計簿_fig5.png)
5a. ![fig5a](/家計簿_fig5a.png)
6. ![fig6](/家計簿_fig6.png)
