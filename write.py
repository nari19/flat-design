def wr(t):
    file_name = "../" + t[0] + ".svg"
    f = open(file_name, 'w', encoding='utf-8')
    # template
    source = '<?xml version="1.0" encoding="utf-8" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" baseProfile="full" version="1.1" viewBox="aaaaa"><rect width="100%" height="100%" fill="bbbbb"/>'
    # ratio
    if t[1] == "0" :
        source = source.replace("aaaaa", "0 0 200 280")
    elif t[1] == "1":
        source = source.replace("aaaaa", "0 0 360 200")
    else:
        source = source.replace("aaaaa", "0 0 300 300")
    # background-color
    source = source.replace("bbbbb", t[2])


    # source += tag.replace("ccccc", t[p+=1]).replace("ddddd", t[p+=1]).replace("eeeee", t[p+=1])
    def rp(tag, p, *args):
        global source
        for i in args:
            source += tag.replace(i, t[p+1])

    # add new
    ty = [u for u, x in enumerate(t) if x == "y"]#add newした時のインデックスを配列化
    for i in range(len(ty)):
        p = ty[i] + 1   #タグの種類を指定する時のインデックス
        if t[p] == "1":     #rect
            tag = '<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>'
            rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff", "ggggg")
        elif t[p] == "2":     #circle
            tag = '<circle cx="ccccc" cy="ddddd" r="eeeee" fill="fffff" />'
            rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff")
        elif t[p] == "3":     #text
            tag = '<text x="ccccc" y="ddddd" font-family="eeeee" font-size="fffff">ggggg</text>'
            rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff", "ggggg")
        elif t[p] == "4":     #path
            tag = '<path d="ccccc" fill="ddddd"/'
            rp(tag, p, "ccccc", "ddddd")
        else:
            break

    # close tag
    source += "</svg>"
    # 書き出し
    f.write(source)
    f.flush()
    f.close()

# "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#b2bec3", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8", "#636e72", "#fdcb6e", "#e17055", "#d63031", "#e84393", "#2d3436"
