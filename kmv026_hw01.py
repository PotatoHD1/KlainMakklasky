def f(x, y):
    return -5 < y < -3 and -1 < x < 9 and ((a := (x + 1) ** 2 + (y + 4) ** 2) == 4 ** 2 or a == 3 ** 2)


def g(a, b, c):
    if b == 0:
        if a != 3 and a != -3:
            if c != 0:
                res = 1
            else:
                res = 0
        else:
            res = "continuum"
    elif a == 0:
        if c != 0:
            if abs(3 * c) == abs(c):
                res = 2
            else:
                res = 3
        else:
            res = 2
    elif c == 0:
        res = 2
    else:
        if (a + 3) * c == b * 5 or (a - 3) * c == b * 5:
            res = 2
        else:
            res = 3
    return str(res)
