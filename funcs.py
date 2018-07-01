#複数のinput関数を同時に呼び出す
def ip(t, *args):
    for i in args:
        t += [input(i)]
    return t



# x = 3
# y = 5

# x1 = "x=" + str(int(x * 200 / 10))
# y1 = "y=" + str(int(y * 280 / 10))

# print(x1)
# print(y1)

