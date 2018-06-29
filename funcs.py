x = 3
y = 5

x1 = "x=" + str(int(x * 200 / 10))
y1 = "y=" + str(int(y * 280 / 10))

print(x1)
print(y1)

def Iput(x, t):
    for i in [x]:
        t += [input(x)]

t = []
Iput("", t)
Iput("r= ; ", t)
Iput("fill= ; ", t)
print(t)