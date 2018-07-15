from funcs import t_edit
"""
main2.py  →エディタ操作で生成
    └── funcs.py
            └── write.py
"""
def callback():
    # ------------------------------
    # temp_color()# funcs.py定義したインデックスカラーをsvgに書き出す
    temp_font()# funcs.py定義したフォントをsvgに書き出す
    # cross_square()# 斜めに正方形を並べる


    # -------------------------------    

# funcs.py定義したインデックスカラーをsvgに書き出す
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
            t += ['y', '3', str(x), 'w'+str(k), 'h'+str(i+1), 'f1', '7', '#2d3436']
            x += 1

    t += ['n']
    t_edit(t)

# funcs.py定義したフォントの種類をsvgに書き出す
def temp_font():
    # ip("text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ;", "fill= ;")
    t = ['temp_font', '1', '#fff']
    for i in range(10):
            t += ['y', '3','c'+str(i+1)+' text-sample テキストサンプル', 'w1', 'h'+str(i+1), 'f'+str(i+1), '10', '#2d3436']

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

callback()


