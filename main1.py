import collections
import pandas as pd
import random


def F2(a):
    newlist = []
    for i in a:
        if i not in newlist:
            newlist.append(i)
    return newlist


def F3(inp, res):
    for i in inp:
        f = F1(bin(i + 16)[3:])
        table[f] = [0] * len(res)
        for j, k in enumerate(res):
            if i in k[0]:
                table[f][j] = 1
    df = pd.DataFrame(data=table, index=[i[1] for i in res])
    return df




def encode(n):
    ALPHABET = \
        "0123456789abcdefghijklmnopqrstuvwxyz"
    try:
        return ALPHABET[n]
    except IndexError:
        raise Exception("cannot encode: %s" % n)


def dec_to_base(dec=0, base=16):
    if dec < base:
        return encode(dec)
    else:
        return dec_to_base(dec // base, base) + encode(dec % base)


def F(a, b):
    count = 0
    k = 0
    for j in range(len(a)):
        # if a[j] != b[j] and not (a[j] == "-" or b[j] == "-"):
        if a[j] != b[j]:
            count += 1
            k = j
    if count == 1:
        a = a[:k] + "-" + a[k + 1:]
        return a
    return ""


def F1(a):
    mas = "abcd"
    res = ""
    for i in range(len(a)):
        if a[i] == "1":
            res += mas[i]
        elif a[i] == "0":
            res += "¬" + mas[i]
    return res


inp = [1, 2, 3, 4, 5, 6, 9, 11, 13, 15]
a = [[], [], [], [], []]
res = []
used = set()
gened = set()
for i in inp:
    f = str(bin(i + 16)[3:])
    unsorted = dict(collections.Counter(f))
    if "1" not in unsorted:
        unsorted['1'] = 0
    a[unsorted['1']].append(([i], f))
print(a)
for o in range(3):
    b = [[], [], [], []]
    for i in range(5 - o):
        for m, j in a[i]:
            if i < 5 - o - 1:
                for l, k in a[i + 1]:
                    if f := F(j, k):
                        used.add(j)
                        used.add(k)
                        if f not in gened:
                            unsorted = dict(collections.Counter(f))
                            if "1" not in unsorted:
                                unsorted['1'] = 0
                            tmp = list(m)
                            tmp[0:0] = l
                            gened.add(f)
                            b[unsorted['1']].append((tmp, f))
            if j not in used:
                res.append((m, j))
    a = b
    print(a)
print(res)
for i in range(len(res)):
    res[i] = (res[i][0], F1(res[i][1]))
print(res)
result = set()
for l in range(2 ** len(res)):
    table = {}
    inp1 = []
    res1 = []
    for i in range(len(res)):
        if str(bin(l + 2 ** len(res)))[3:][i] == "1":
            res1.append(res[i])
    for i in inp:
        f = F1(bin(i + 16)[3:])
        table[f] = 0
        for k in res1:
            if i in k[0]:
                # print(k[0])
                table[f] += 1
    temp = ""
    for k in res1:
        temp += k[1] + "V"
    temp = temp[:-1]
    # print(inp1)
    if all([i > 0 for i in table.values()]):
        if not temp in result:
            result.add(temp)
            df = F3(inp, res1)
            df.to_excel(f"output{l}.xlsx")
            print(temp, [i for i in range(len(res)) if str(bin(l + 2 ** len(res)))[3:][i] == "1"])
            # print(result)
print(result)
# for i in inp:
#     f = F1(bin(i + 16)[3:])
#     table[f] = [0] * len(res)
#     for j, k in enumerate(res):
#         if i in k[0]:
#             table[f][j] = 1
# df = pd.DataFrame(data=table, index=[i[1] for i in res])
# df.to_excel("output.xlsx")
