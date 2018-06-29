
for i in ["#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#b2bec3", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8", "#636e72", "#fdcb6e", "#e17055", "#d63031", "#e84393", "#2d3436"]:
    # --------------------
    file_name = "images/" + i + ".svg"
    ratio = "tate" 
    # --------------------
    f = open(file_name, 'w', encoding='utf-8')
    if ratio == "tate":
        c0 = '<?xml version="1.0" encoding="utf-8" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" baseProfile="full" version="1.1" viewBox="0 0 200 280"><rect width="100%" height="100%" fill="aaaaa"/></svg>'
    elif ratio == "yoko":
        c0 = '<?xml version="1.0" encoding="utf-8" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" baseProfile="full" version="1.1" viewBox="0 0 360 200"><rect width="100%" height="100%" fill="aaaaa"/></svg>'
    else:
        c0 = '<?xml version="1.0" encoding="utf-8" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" baseProfile="full" version="1.1" viewBox="0 0 300 300"><rect width="100%" height="100%" fill="aaaaa"/></svg>'
    source = c0.replace("aaaaa", i)

    print (i)

    f.write(source)
    f.flush()
    f.close()