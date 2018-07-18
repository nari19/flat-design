from funcs import t_edit
"""
main2.py  →(エディタ操作で生成)
    └── funcs.py
            └── write.py
"""
def callback():# 関数の前方参照を行う
    # ------------------------------------------------------------
    normal()# 配列をターミナル以外でそのまま定義
    # temp_color()# funcs.pyで定義したインデックスカラーを書き出す
    # temp_font()# funcs.pyで定義したフォントを書き出す
    # cross_square()# 斜めに正方形を並べる


    # -------------------------------------------------------------

# 配列をターミナル以外でそのまま定義
def normal():
    t = ['noraml', '1', '#fff']
    # rect "1"   ("x= ; ", "y= ; ", "width= ; ", "height= ; ", "fill= ; ")
    # circle "2" ("cx= ; ", "cy= ; ", "r= ; ", "fill= ; ")
    # text "3"   ("text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ;", "fill= ;")
    # path "4"   ("d= ; ", "fill= ; ")
    t += ['y', '3','text', 'w1', 'h1', 'f1', '7', '#00cec9']
    t += ['n']
    t_edit(t)


# funcs.pyで定義したインデックスカラーを書き出す
def temp_color():
    t = ['temp_color', '3', '#fff']
    x = 1
    # 色を並べる
    for i in range(10):
        for k in range(10):
            t += ['y', '1', 'w'+str(k), 'h'+str(i), 'w1', 'h1', 'c'+str(x)]
            x += 1
    # 数字を並べる
    x = 1
    for i in range(10):
        for k in range(10):
            t += ['y', '3', ' c'+str(x), 'w'+str(k), 'h'+str(i+1), 'f1', '7', '#2d3436']
                          #  ↑cnがfuncs.pyで変換されないように空白を空ける
            x += 1
    t += ['n']
    t_edit(t)


# funcs.pyで定義したフォントの種類を書き出す
def temp_font():
    # ip("text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ;", "fill= ;")
    t = ['temp_font', '1', '#fff']
    h = 18
    for i in range(10):
            # フォントの種類を記述
            t += ['y', '3','f'+str(i+1), 'w1', str(h), 'f'+str(i+1), '7', '#00cec9']
            # 'sample-text'と文字を記述
            t += ['y', '3','f'+str(i+1)+' text-sample テキストサンプル', 'w1', 'h'+str(i+1), 'f'+str(i+1), '10', '#2d3436']
            h += 28
    t += ['n']
    t_edit(t)


# 斜めに正方形を並べる
def cross_square():
    t = ['cross_square2', '3', '#fff']
    x = 1
    for i in range(10):
        t += ['y', '1', 'w'+str(i), 'h'+str(i), 'w1', 'h1', 'c'+str(x)]
        x += 1
    t += ['n']
    t_edit(t)


# 関数の前方参照を行う(一番下に置く)
callback()


