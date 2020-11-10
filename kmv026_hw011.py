def to_tuple(a):
    if type(a) == tuple:
        return a
    m_a = get_count(a)
    if str(a).__contains__("e"):
        res = str(a).replace(".", "").split('e')[0]
    else:
        res = str(a).replace(".", "")
    return (m_a, int(res))


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
        if type(a) == type(self):
            self.m_p, self.m = a.asTuple()
        else:
            self.m_p, self.m = to_tuple(a)
            self.remove_zeros()

    def remove_zeros(self):
        if self.m != 0:
            while self.m % 10 == 0:
                self.m_p -= 1
                self.m //= 10
        else:
            self.m_p = 0
        return self

    def __add__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = LongFloat(other).asTuple()
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        return LongFloat((m_c, a + other)).remove_zeros()

    def __pow__(self, n):
        if type(n) == int:
            if n > 0:
                return LongFloat((self.m_p * n, self.m ** n)).remove_zeros()
            else:
                return LongFloat((self.m_p * n, self.m ** n)).remove_zeros()

    def __bool__(self):
        if self.m_p == 0 and self.m == 1:
            return True
        return False

    def __ceil__(self):
        sng = 1 if self.m >= 0 else -1
        if self.m_p > len(str(self.m)):
            res = sng
        elif self.m_p < 0:
            res = self.m * 10 ** -self.m_p
        else:
            res = divmod(abs(self.m), 10 ** self.m_p)
            res = int(res[0]), int(res[1])
            res = sng * (res[0] + (1 if res[1] != 0 else 0))
            if sng < 0:
                res += 1
        return res

    def __floor__(self):
        sng = 1 if self.m >= 0 else -1
        if self.m_p > len(str(self.m)):
            if sng == 1:
                res = 0
            else:
                res = -1
        elif self.m_p < 0:
            res = self.m * 10 ** -self.m_p
        else:
            res = divmod(abs(self.m), 10 ** self.m_p)
            res = int(res[0]), int(res[1])
            res = sng * (res[0] + (1 if res[1] != 0 else 0))
            if sng > 0 and self.m != 0:
                res -= 1
        return res

    def __int__(self):
        return self.__floor__() if self >= 0 else self.__ceil__()

    def __abs__(self):
        return LongFloat((self.m_p, abs(self.m)))

    def __eq__(self, other):
        if isinstance(other, (int, float, type(self), tuple)):
            return LongFloat(other).asTuple() == self.asTuple()
        else:
            return False

    def as_integer_ratio(self):
        print("a")

    def __truediv__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = LongFloat(other).asTuple()
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        i = 0
        while a % other != 0 and i <= 1000:
            a *= 10
            m_c += 1
            i += 1
        return LongFloat((m_c, a // other)).remove_zeros()

    def __divmod__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = LongFloat(other).asTuple()
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        res = divmod(a, other)
        return (LongFloat((m_c, res[0])).remove_zeros(), LongFloat((m_c, res[1])).remove_zeros())

    def __mod__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = LongFloat(other).asTuple()
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        return LongFloat((m_c, a % other)).remove_zeros()

    def __floordiv__(self, other):
        m_a, a = self.m_p, self.m
        m_other, other = LongFloat(other).asTuple()
        m_c = max(m_a, m_other)
        a *= 10 ** (m_c - m_a)
        other *= 10 ** (m_c - m_other)
        return LongFloat((m_c, a // other)).remove_zeros()

    def __round__(self, n=None):
        if n is None:
            n = 0
        temp = self * 10 ** n
        print(abs(temp - int(temp)))
        if abs(temp - int(temp)) >= 0.5:
            if self >= 0:
                temp = temp.__ceil__() / 10 ** n
            else:
                temp = temp.__floor__() / 10 ** n
        else:
            if self < 0:
                temp = temp.__ceil__() / 10 ** n
            else:
                temp = temp.__floor__() / 10 ** n
        return LongFloat(temp).remove_zeros()

    def __reversed__(self):
        return LongFloat(1) / self

    def __neg__(self):
        return LongFloat((self.m_p, -self.m))

    def __sub__(self, other):
        return self + (-LongFloat(other))

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, (int, float, type(self), tuple)):
            return (self - LongFloat(other)).asTuple()[1] < 0

    def __le__(self, other):
        if isinstance(other, (int, float, type(self), tuple)):
            return (self - LongFloat(other)).asTuple()[1] <= 0

    def __gt__(self, other):
        if isinstance(other, (int, float, type(self), tuple)):
            return (self - LongFloat(other)).asTuple()[1] > 0

    def __ge__(self, other):
        if isinstance(other, (int, float, type(self), tuple)):
            return (self - LongFloat(other)).asTuple()[1] >= 0

    def asTuple(self):
        return (self.m_p, self.m)

    def __mul__(self, other):
        m_other, other = LongFloat(other).asTuple()
        return LongFloat((self.m_p + m_other, self.m * other)).remove_zeros()

    def __str__(self):
        res = str(abs(self.m))
        if self.m_p != 0:
            if not -8 <= self.m_p < len(res):
                if len(res) > 1:
                    res = res[0] + '.' + res[1:]
                m_a = -self.m_p + get_count(res)
                res = res + 'e' + str(m_a)
            else:
                res = res[:len(res) - self.m_p] + ('.' if len(res) > 1 else '') + res[len(
                    res) - self.m_p:] + '0' * -self.m_p
        if self.m < 0:
            res = '-' + res
        return f"LongFloat({res})"


a = LongFloat(10)
a **= 2
print(round(-a + 0.5))
