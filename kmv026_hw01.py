def F1(a, n=2):
    m_a, a = a
    return m_a * n, a ** n


def F2(a):
    m_a = get_count(a)
    if str(a).__contains__("e"):
        res = str(a).replace(".", "").split('e')[0]
    else:
        res = str(a).replace(".", "")
    return m_a, int(res)


def get_count(number):
    if str(number).__contains__("."):
        if not str(number).__contains__("e"):
            leng = len(str(number).split('.')[1])
        else:
            tmp = str(number).split('.')[1].split('e')
            leng = len(tmp[0]) - int(tmp[1])
    else:
        if not str(number).__contains__("e"):
            leng = 0
        else:
            leng = -int(str(number).split('e')[1])
    return leng


def F(a, b):
    m_a, a = a
    m_b, b = b
    m_c = max(m_a, m_b)
    a *= 10 ** (m_c - m_a)
    b *= 10 ** (m_c - m_b)
    return m_c, a + b


def f(x, y):
    if -5 < y < -3 and -1 < x < 9:
        a = F(F1(F(F2(x), F2(1.0))), F1(F(F2(y), F2(4.0))))
        if F(a, F2(-6 ** 2))[1] == 0 or F(a, F2(-8 ** 2))[1] == 0:
            return True
    return False


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
