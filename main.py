def F(f):
    a, b, c = map(int, f)
    return (not (a ^ (not b))) or (not c)


[print(i, f) for i in range(8) if F(f := str(bin(i + 8))[3:])]