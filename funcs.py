#複数のinput関数を同時に呼び出す
def ip(t, *args):
    for i in args:
        t += [input(i)]
    return t

# source += tag.replace("ccccc", t[p+=1]).replace("ddddd", t[p+=1]).replace("eeeee", t[p+=1])
# 関数化
def rp(*args):
    for i in args:
        sourse += tag.replace(i, t[p+=1])
    return source

# x = 3
# y = 5

# x1 = "x=" + str(int(x * 200 / 10))
# y1 = "y=" + str(int(y * 280 / 10))

# print(x1)
# print(y1)

