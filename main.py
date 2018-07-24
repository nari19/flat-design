from funcs import t_edit
"""
 main.py  →(ターミナルでの対話入力で生成)
    └── funcs.py
            └── write.py
"""

t = []
#複数のinput関数を同時に呼び出す
def ip(*args):
    global t
    for i in args:
        t += [input(i)]

ip("file name; ", "1:vertical 2:oblong 3:square; ", "background; ")
t_edit(t)
ip("add new? y/n; ")

while t[-1] == "y":
    ip("1:rect 2:circle 3:text 4:path; ")
    if t[-1] == "1":
        # rect
        ip("x= ; ", "y= ; ", "width= ; ", "height= ; ", "fill= ; ")
    elif t[-1] == "2":
        # circle
        ip("cx= ; ", "cy= ; ", "r= ; ", "fill= ; ")
    elif t[-1] == "3":
        # text
        ip("text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ;", "fill= ;")
    elif t[-1] == "4":
        # path
        ip("d= ; ", "fill= ; ")
    else :
        print("not command!")
        break
    t_edit(t)   #要素を追加するごとにファイルを上書き
    ip("add new? y/n;")

print(t)
t_edit(t)
# csv(t)

# memo
"""
・main2の関数からmainの後半を関数にしたものを繋げる。
	それにより柔軟に対話型入力を取り入れる
・main2の関数一覧をエディタ内のコメントアウトで操作するのではなく
	input関数の別の機能で、関数をターミナルの中から選べせる
	ように変える。
・temp_font, temp_colorをブラウザで実装
・inputで予期しない値が入力された場合に、もう一度その操作を繰り返す
	例外処理を実装する。
・pathデータで花のデザインをする。
・デザインの機械学習
・スクレイピングで英語テキストを取得
・静的サイトジェネレータの考え方で活用
・値を時間で操作してアニメーション→ユーザの選択をより簡単にする。
・cuiでのsvg操作を完了させる→pythonサーバーで登録した色、フォンとを
    ブラウザで表示する
・foreignobjectを可能にし、htmlで入力させる
・html, svg, css scriptをそれぞれ入力
アプリケーション作成
    構図と配色を決めてくれる、画像を作成、htmlの問題を作ってくれる
    テンプレートの共有
"""