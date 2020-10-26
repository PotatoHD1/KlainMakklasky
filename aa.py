res = [([3, 2], '¬a¬bc'), ([6, 2], '¬ac¬d'), ([5, 4], '¬ab¬c'), ([6, 4], '¬ab¬d'), ([11, 9, 3, 1], '¬bd'),
       ([13, 9, 5, 1], '¬cd'), ([15, 13, 11, 9], 'ad')]
inp = [1, 2, 3, 4, 5, 6, 9, 11, 13, 15]
tablo = {'¬a¬b¬cd': 2, '¬a¬bc¬d': 2, '¬a¬bcd': 2, '¬ab¬c¬d': 2, '¬ab¬cd': 2, '¬abc¬d': 2, 'a¬b¬cd': 3, 'a¬bcd': 2,
         'ab¬cd': 2, 'abcd': 1}


def F1(a):
    mas = "abcd"
    res = ""
    for i in range(len(a)):
        if a[i] == "1":
            res += mas[i]
        elif a[i] == "0":
            res += "¬" + mas[i]
    return res


def F4(table, inp, res):
    temp = dict(table)
    print(table)
    print(res)
    print(inp)
    print()
    for k in res:
        table = dict(temp)
        for i in inp:
            f = F1(bin(i + 16)[3:])
            if i in k[0]:
                table[f] -= 1
        print(table)
        if all([i > 0 for i in table.values()]):
            return False
    return True

print(len({'¬a¬bcV¬ab¬dV¬bdV¬cdVad', '¬a¬bcV¬ac¬dV¬ab¬dV¬cdVad', '¬a¬bcV¬ab¬cV¬ab¬dV¬bdV¬cdVad', '¬ac¬dV¬ab¬cV¬bdVad',
           '¬a¬bcV¬ac¬dV¬ab¬cV¬ab¬dV¬cdVad', '¬ac¬dV¬ab¬cV¬ab¬dV¬bdV¬cdVad', '¬a¬bcV¬ab¬cV¬ab¬dV¬bdVad',
           '¬a¬bcV¬ac¬dV¬ab¬cV¬cdVad', '¬a¬bcV¬ab¬dV¬cdVad', '¬ac¬dV¬ab¬cV¬ab¬dV¬bdVad',
           '¬a¬bcV¬ac¬dV¬ab¬cV¬ab¬dV¬bdV¬cdVad', '¬ac¬dV¬ab¬cV¬bdV¬cdVad', '¬a¬bcV¬ab¬cV¬ab¬dV¬cdVad',
           '¬a¬bcV¬ac¬dV¬ab¬cV¬bdVad', '¬a¬bcV¬ac¬dV¬ab¬cV¬bdV¬cdVad', '¬ac¬dV¬ab¬dV¬bdV¬cdVad',
           '¬a¬bcV¬ac¬dV¬ab¬cV¬ab¬dV¬bdVad', '¬a¬bcV¬ac¬dV¬ab¬dV¬bdV¬cdVad'}))
# if all([i > 0 for i in table.values()]) and F4(table, inp, res1) and not temp in result:
#     result.add(temp)
#     print(temp)
#     # print(result)
