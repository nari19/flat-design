from main import t
from write import wr


def t_edit(t):
    cn = {
        'c1': "#55efc4", 'c2': "#81ecec", 'c3': "#74b9ff", 'c4': "#a29bfe", 'c5': "#dfe6e9", 
        'c6': "#00b894", 'c7': "#00cec9", 'c8': "#0984e3", 'c9': "#6c5ce7", 'c10': "#b2bec3",
        'c11': "#ffeaa7", 'c12': "#fab1a0", 'c13': "#ff7675", 'c14': "#fd79a8", 'c15': "#636e72", 
        'c16': "#fdcb6e", 'c17': "#e17055", 'c18': "#d63031", 'c19': "#e84393", 'c20': "#2d3436"
    }
    fn = {'f1': "Menlo", 'f2': "Monaco", 'f3': "M+ 1c light", 'f4': "M+ 1plight", 'f5': "Myra 4F Caps Bold"}
    
    if t[1] == "1":
        w = 20
        h = 28
    elif t[1] == "2":
        w = 36
        h = 20
    else :
        w = 30
        h = 30
    for i in range(10):
        sn["s" + i] = w * i
    print(sn)
    sn = {s1: "30", s2: "60", s3: "90" }
    for i in range(len(t)):
        for k in cn:
            if t[i] == k:
                t[i] = cn[k]
        for k in fn:
            if t[i] == k:
                t[i] = sn[k]
        

    



    wr(t)
    # ['hoge', '1', '#33a', 'y', '2', '0', '0', '100', 'red', 'n']
# a = '5'
# d = {a: int(a)*30}
# print(d[a])
    # (tのインデント) = (アルファベットと数字の2文字を抽出する正規表現)
    # for (条件:)
    # t[] = t[] * 200 / 10
    # pixel
    # p1 = x * 200 / 10
    # # color
    # c1 = "#55efc4"
    # c2 = "#81ecec"
    # c3 = "#74b9ff"
    # font

# 配色インデックスカラー
# px比率
# 例外処理
# ブラウザ確認
# foreignObject要素 html
# script, style
# x = 3
# y = 5

# x1 = "x=" + str(int(x * 200 / 10))
# y1 = "y=" + str(int(y * 280 / 10))
# s = int(input("s: "))
# print(s * 20)

# print(x1)
# print(y1)


# "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#b2bec3", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8", "#636e72", "#fdcb6e", "#e17055", "#d63031", "#e84393", "#2d3436"