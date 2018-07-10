# svgファイル書き出し
def wr(t):
    file_name = "../" + t[0] + ".svg"
    f = open(file_name, 'w', encoding='utf-8')
    
    # template
    source = '<?xml version="1.0" encoding="utf-8" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" baseProfile="full" version="1.1" viewBox="aaaaa"><rect width="100%" height="100%" fill="bbbbb"/>'
    # ratio
    if t[1] == "1" :
        source = source.replace("aaaaa", "0 0 200 280")
    elif t[1] == "2":
        source = source.replace("aaaaa", "0 0 360 200")
    else:
        source = source.replace("aaaaa", "0 0 300 300")
    # background-color
    source = source.replace("bbbbb", t[2])

    # source += tag.replace("ccccc", t[p+=1]).replace("ddddd", t[p+=1]).replace("eeeee", t[p+=1])
    def rp(tag, p, *args):
        for i in args:
            p += 1
            tag = tag.replace(i, t[p])
        return tag

    # add new
    ty = [u for u, x in enumerate(t) if x == "y"]#add newした時のインデックスを配列化
    for i in range(len(t)):
        p = ty[i] + 1   #タグの種類を指定する時のインデックス
        if t[p] == "1":     #rect
            tag = '<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>'
            source += rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff", "ggggg")
        elif t[p] == "2":     #circle
            tag = '<circle cx="ccccc" cy="ddddd" r="eeeee" fill="fffff" />'
            source += rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff")
        elif t[p] == "3":     #text
            tag = '<text x="ddddd" y="eeeee" font-family="fffff" font-size="ggggg">ccccc</text>'
            source += rp(tag, p, "ccccc", "ddddd", "eeeee", "fffff", "ggggg")
        elif t[p] == "4":     #path
            tag = '<path d="ccccc" fill="ddddd"/'
            source += rp(tag, p, "ccccc", "ddddd")
        else:
            break
            
    # close tag
    source += "</svg>"
    # 書き出し
    f.write(source)
    f.flush()
    f.close()


# csvファイル書き出し
def csv(t):
    file_name = "test.csv"
    f = open(file_name, 'a', encoding='utf-8')
    writeCsv = ""
    for i in t:
        writeCsv += i + ","
    # 書き出し
    print(writeCsv)
    f.write(t)
    f.flush()
    f.close()