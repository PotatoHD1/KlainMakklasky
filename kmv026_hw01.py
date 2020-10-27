from decimal import *


def F1(a, n=2):
    m_a, a = a
    return m_a * n, a ** n


def F2(a):
    m_a = get_count(a)
    return m_a, int(round(a * 10 ** m_a))


def get_count(number):
    return Decimal(str(number)).as_tuple().exponent * (-1)


def F(a, b):
    m_a, a = a
    m_b, b = b
    # print(m_a, m_b)
    m_c = max(m_a, m_b)
    a *= 10 ** (m_c - m_a)
    b *= 10 ** (m_c - m_b)
    return m_c, a + b


def f(x, y):
    # a = F(F1(F(x, 1.0)), F1(F(y, 4.0)))
    if -5 < y < -3 and -1 < x < 9:
        a = (Decimal(x) + 1) ** 2 + (Decimal(y) + 4) ** 2
        print(a)
        if (a == Decimal(6 ** 2) or a == Decimal(8 ** 2)):
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
print("%.60f" % 1.2399)
