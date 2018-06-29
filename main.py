import funcs as fu
t = []
fu.ip(t, "file name; ", "1:vertical 2:oblong 3:square; ", "background; ", "add new? y/n; ")
print(t)
while t[-1] == "y":
    t += [input("1:rect 2:circle 3:text 4:path; ")]
    if t[-1] == "1":
        # rect
        t += [input("x= ; ")]
        t += [input("y= ; ")]
        t += [input("width= ; ")]
        t += [input("height= ; ")]
        t += [input("fill= ; ")]     
    elif t[-1] == "2":
        # circle
        t += [input("cx= ; ")]
        t += [input("cy= ; ")]
        t += [input("r= ; ")]
        t += [input("fill= ; ")]   
    elif t[-1] == "3":
        # text
        t += [input("text ; ")]
        t += [input("x= ; ")]
        t += [input("y= ; ")]
        t += [input("font-family= ; ")]
        t += [input("font-size= ; ")]
    elif t[-1] == "4":
        # text
        t += [input("text ; ")]
        t += [input("x= ; ")]
        t += [input("y= ; ")]
        t += [input("font-family= ; ")]
        t += [input("font-size= ; ")]
        break
    else :
        break
    t += [input("add new? y/n; ")]


print(t)


