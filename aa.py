import numpy as np
import pandas as pd
import csv
import numpy, scipy
from scipy.spatial import distance
import subprocess
import os

lenth = 5
time = 5
wen = [0] * time
Dbm = 11
running = []
i = 0
afirst = [0] * lenth
asec = [0] * lenth
b = [[0] * (Dbm) for t in range(time)]
currentmass = []
new = [[0] * (Dbm - 6) for i in range(time)]
wen = [[0] * (Dbm - 6) for i in range(time)]
first = []
second = []
finalres = 10000000000000000000000
res = [0] * time
euclidean = 0
Database = []
finalrescurrent = 0


def euclidean(name_in_data, current_name):
    global time, wen, Dbm, running, i, a, b, currentmass, new, first, second, finalres, res, euclidean, Database, afirst, asec

    def average(mass):
        s = 0
        N = len(mass)
        s = sum(mass)
        return s / N

    def foo(a):
        global new
        for i in range(time):
            for j in range(Dbm - 6):
                new[i][j] = int(a[i][j + 6])
        return new

    def foo1(b):
        global wen
        for i in range(time):
            for j in range(Dbm - 6):
                wen[i][j] = int(b[i][j + 6])
        return wen

    with open('recording.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            asec[i] = row
            i += 1
    currentmass = foo1(asec)
    i = 0

    with open(name_in_data, 'rt')as f:
        data = csv.reader(f)
        for row in data:
            afirst[i] = row
            i += 1
    running = foo(afirst)
    print(running)
    print(currentmass)
    for h in range(time):
        first = running[h]
        second = currentmass[h]
        euclidean = scipy.spatial.distance.euclidean(first, second)
        res[h] = euclidean
        if average(res) <= finalres:
            finalres = average(res)
    print(finalres)
    lenth = 5
    time = 5
    wen = [0] * time
    Dbm = 11
    running = []
    i = 0
    afirst = [0] * lenth
    asec = [0] * lenth
    b = [[0] * (Dbm) for t in range(time)]
    currentmass = []
    new = [[0] * (Dbm - 6) for i in range(time)]
    wen = [[0] * (Dbm - 6) for i in range(time)]
    first = []
    second = []
    res = [0] * time
    euclidean = 0
    Database = []
    finalrescurrent = 0
    return finalres


current_name = 'recording.csv'
os.chdir("D:\Data")
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        Name = (os.path.join(root, name))
        name_in_data = str(Name[2:])
        euclidean(name_in_data, current_name)
