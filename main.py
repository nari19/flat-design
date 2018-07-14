from funcs import t_edit
"""
.
├── README.md
├── __pycache__
├── main.py
|
├── main2.py
|
├── funcs.py
|
└── write.py
"""

t = []
#複数のinput関数を同時に呼び出す
def ip(*args):
    global t
    for i in args:
        t += [input(i)]

ip("file name; ", "1:vertical 2:oblong 3:square; ", "background; ")
t_edit(t)
ip("add new? y/n; ")

while t[-1] == "y":
    ip("1:rect 2:circle 3:text 4:path; ")
    if t[-1] == "1":
        # rect
        ip("x= ; ", "y= ; ", "width= ; ", "height= ; ", "fill= ; ")
    elif t[-1] == "2":
        # circle
        ip("cx= ; ", "cy= ; ", "r= ; ", "fill= ; ")
    elif t[-1] == "3":
        # text
        ip("text ; ", "x= ; ", "y= ; ", "font-family= ; ", "font-size= ;", "fill= ;")
    elif t[-1] == "4":
        # path
        ip("d= ; ", "fill= ; ")
    else :
        print("not command!")
        break
    t_edit(t)   #要素を追加するごとにファイルを上書き
    ip("add new? y/n;")

print(t)
t_edit(t)
# csv(t)