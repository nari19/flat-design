from write import wr

# 頻繁に使う色やフォントを簡単な文字列で定義する
def t_edit(t):
    # ------------------------------------------------------------------------------------------------------
    # アルファベットと数字のキーを指定して色とフォントの要素を追加する
    cn = {
        'c1': "#55efc4", 'c2': "#81ecec", 'c3': "#74b9ff", 'c4': "#a29bfe", 'c5': "#dfe6e9", 
        'c6': "#00b894", 'c7': "#00cec9", 'c8': "#0984e3", 'c9': "#6c5ce7", 'c10': "#b2bec3",
        'c11': "#ffeaa7", 'c12': "#fab1a0", 'c13': "#ff7675", 'c14': "#fd79a8", 'c15': "#636e72", 
        'c16': "#fdcb6e", 'c17': "#e17055", 'c18': "#d63031", 'c19': "#e84393", 'c20': "#2d3436",
        'c21': "#ffffff"
    }
    fn = {'f1': "Menlo", 'f2': "Monaco", 'f3': "M+ 1c light", 'f4': "M+ 1plight", 'f5': "Myra 4F Caps Bold"}
    # ------------------------------------------------------------------------------------------------------

    # 選んだ縦横比ごとに10等分した要素を指定  wn:横幅比率  hn:縦幅比率
    if t[1] == "1":
        w = 20
        h = 28
    elif t[1] == "2":
        w = 36
        h = 20
    else:
        w = 30
        h = 30
    wn = {}
    for i in range(11):
        wn["w" + str(i)] = str(w * i)
    hn = {}
    for i in range(11):
        hn["h" + str(i)] = str(h * i)

    # tの配列を事前に定義したキーワードに書き換える
    for i in range(len(t)):
        for k in cn:
            if t[i] == k:
                t[i] = cn[k]
        for k in fn:
            if t[i] == k:
                t[i] = fn[k]
        for k in wn:
            if t[i] == k:
                t[i] = wn[k]
        for k in hn:
            if t[i] == k:
                t[i] = hn[k]
    wr(t)
# ['hoge', '1', '#33a', 'y', '2', '0', '0', '100', 'red', 'n']
# "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#b2bec3", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8", "#636e72", "#fdcb6e", "#e17055", "#d63031", "#e84393", "#2d3436"
# 標準入力を正しい値が出るまで繰り返す
# https://qiita.com/u1and0/items/66a72fef8bc0a7ce5eda


