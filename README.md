# 勾配法：反復による最小値探索
データ[[2,4],[4,2]]に直線y=w*xをフィットさせる⇔損失関数（誤差の二乗和）を最小にするパラメータ（傾きw）を探す
## 学習率0.01（収束）
![gd01](/gradient_descent_01.gif)
## 0.01（谷の反対側の初期値から収束）
![gd01a](/gradient_descent_01a.gif)
## 0.04（谷を行ったり来たり収束）
![gd04](/gradient_descent_04.gif)
## 0.06（発散）
![gd06](/gradient_descent_06.gif)
