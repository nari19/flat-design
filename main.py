import write
import funcs as fu
t = []
fu.ip(t, "file name; ", "1:vertical 2:oblong 3:square; ", "background; ", "add new? y/n; ")
while t[-1] == "y":
    fu.ip(t, "1:rect 2:circle 3:text 4:path; ")
    print(t)
    if t[-1] == "1":
        # rect
        fu.ip(t, "x= ; ", "y= ; ", "width= ; ", "height= ; ", "fill= ; ")
    elif t[-1] == "2":
        # circle
        fu.ip(t, "cx= ; ", "cy= ; ", "r= ; ", "fill= ; ")
    elif t[-1] == "3":
        # text
        fu.ip(t, "text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ; ")
    elif t[-1] == "4":
        # path
        fu.ip(t, "d= ; ", "fill= ; ")
    else :
        break
    t += [input("add new? y/n; ")]

print(t)
# write.wr(t)


