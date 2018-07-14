from funcs import t_edit


# funcs.py定義したインデックスカラーをsvgに書き出す
def t_temp():
    t = ['template2', '3', '#fff']
    x = 1
    for i in range(10):
        for k in range(10):
            t += ['y', '1', 'w'+str(k), 'h'+str(i), 'w1', 'h1', 'c'+str(x)]
            x += 1

    t += ['n']
    t_edit(t)

# 斜めに正方形を並べる
def cross_square():
    t = ['cross_square', '3', '#fff']
    x = 1
    for i in range(10):
        t += ['y', '1', 'w'+str(i), 'h'+str(i), 'w1', 'h1', 'c'+str(x)]
        x += 1

    t += ['n']
    t_edit(t)




# ------------------------------
# t_temp()
cross_square()


# -------------------------------