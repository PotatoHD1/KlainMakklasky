def to_tuple(a):
    if type(a) == tuple:
        return a
    m_a = get_count(a)
    if str(a).__contains__("e"):
        res = str(a).replace(".", "").split('e')[0]
    else:
        res = str(a).replace(".", "")
    return remove_zeros((m_a, int(res)))


def remove_zeros(a):
    m_a, a = a
    if a != 0:
        while a % 10 == 0:
            m_a -= 1
            a //= 10
    return m_a, a


def get_count(a):
    if a == 0:
        return 0
    if str(a).__contains__("."):
        if not str(a).__contains__("e"):
            leng = len(str(a).split('.')[1])
        else:
            tmp = str(a).split('.')[1].split('e')
            leng = len(tmp[0]) - int(tmp[1])
    else:
        if not str(a).__contains__("e"):
            leng = 0
        else:
            leng = -int(str(a).split('e')[1])
    return leng


class LongFloat(object):

    def __init__(self, a):
        self.m_p, self.m = to_tuple(a)

    def __add__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = to_tuple(other)
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        return LongFloat((m_c, a + other))

    def __pow__(self, n):
        if type(n) == int:
            if n > 0:
                return LongFloat(remove_zeros((self.m_p * n, self.m ** n)))
            else:
                return LongFloat(remove_zeros((self.m_p * n, self.m ** n)))

    def __bool__(self):
        if self.m_p == 0 and self.m == 1:
            return True
        return False

    def __ceil__(self):
        sng = 1 if self.m >= 0 else -1
        if self.m_p > len(str(self.m)):
            res = sng
            if self.m == 0:
                res = 0
        elif self.m_p < 0:
            res = self.m * 10 ** -self.m_p
        else:
            res = divmod(abs(self.m), 10 ** self.m_p)
            res = int(res[0]), int(res[1])
            res = sng * (res[0] + (1 if res[1] != 0 else 0))
            if sng < 0:
                res += 1
        return res

    def __abs__(self):
        return LongFloat((self.m_p, abs(self.m)))

    def asTuple(self):
        return (self.m, self.m_p)

    def __mul__(self, other):
        m_other, other = to_tuple(other)
        return LongFloat(remove_zeros((self.m_p + m_other, self.m * other)))

    def __str__(self):
        res = str(self.m)
        if self.m_p != 0:
            if not -8 <= self.m_p < len(res):
                if len(res) > 1:
                    res = res[0] + '.' + res[1:]
                m_a = -self.m_p + get_count(res)
                res = res + 'e' + str(m_a)
            else:
                res = res[:len(res) - self.m_p] + ('.' if len(res) > 1 else '') + res[len(
                    res) - self.m_p:] + '0' * -self.m_p
        return f"LongFloat({res})"


a = LongFloat(10)
a *= -2
print(a.__ceil__())
