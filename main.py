def F(f):
    a, b, c, d = map(int, f)
    return b and d and a or not b and d or not d and c and not a or b and not a and not c


[print(i, f) for i in range(16) if F(f := str(bin(i + 16))[3:])]
