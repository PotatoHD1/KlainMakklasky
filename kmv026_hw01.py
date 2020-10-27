from math import e


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
    a = F(F1(F(x, 1.0)), F1(F(y, 4.0)))
    if -5 < y < -3 and -1 < x < 9:
        if F(a, F2(-6 ** 2))[1] == 0 or F(a, F2(-8 ** 2))[1] == 0:
            return True
    return False


# print(a)
# while (a[1] != 0):
#     while (a[1] > 0):
#         # print(F(a, F2(-(8 ** 2)))[1])
#         i += 1
#         a = F(F(F1(F(F2(6.99), F2(1.0))), F1(F(F2(Decimal(num + alph[i])), F2(4.0)))), F2(-(8 ** 2)))
#     print(num)
#     print(a)
#     num = num + alph[i]
#     # print(num)
#     i = 0
#     a = F(F(F1(F(F2(6.99), F2(1.0))), F1(F(F2(Decimal(num + alph[i])), F2(4.0)))), F2(-(8 ** 2)))
# print(a)
# print(num)

# print(f(1.000000000000001, 1))
print(F(F1(F2(8.0), 100), F2(-8 ** 100)))
