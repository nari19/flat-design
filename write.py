def wr(t):
    file_name = "images/" + t[0] + ".svg"
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
    # add new
    i = 3
    while t[i] = "y" 
        i += 1
        if t[i] == "1":     #rect
            tag = "<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>"
            source += tag.replace("", )
            i +=  6
        elif t[i] == "2":     #circle
            tag = "<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>"
            source += tag.replace("", )
            i +=  6
        elif t[i] == "3":     #text
            tag = "<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>"
            source += tag.replace("", )
            i +=  6
        elif t[i] == "4":     #path
            tag = "<rect x="ccccc" y="ddddd" width="eeeee" height="fffff" fill="ggggg"/>"
            source += tag.replace("", )
            i +=  6
        else:

        

    # close tag
    source += "</svg>"
    f.write(source)
    f.flush()
    f.close()

# "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#b2bec3", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8", "#636e72", "#fdcb6e", "#e17055", "#d63031", "#e84393", "#2d3436"
