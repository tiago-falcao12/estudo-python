from dis import dis

b = 6


def f2(a):
    global b
    print(a)
    print(b)
    b = 9


print(dir())
