import numpy as np
import pandas as pd
from modulZ1 import fp, P_Geometry
import csv

rng = np.random.default_rng(1000)
N = 1000
R = 10
d = R / 30

X = np.array([])
Y = np.array([])
RES = np.array([])
for i in range(N):
    x = rng.uniform(low=-R - d, high=R * 2 + d)
    y = rng.uniform(low=-R - d, high=R + d)
    res = fp(x, y)

    X = np.append(X, x)
    Y = np.append(Y, y)
    RES = np.append(RES, res)

matrix = np.array([X, Y, RES])
matrix = matrix.transpose()
df = pd.DataFrame(data=matrix)
df.to_excel('BetaTest.xlsx', header=False)
df.to_csv('BetaTest.csv')

with open('BetaTest.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

with open('Sravnenie.txt', 'a') as file:
    PT = P_Geometry(R)
    for i in range(7):
        p = []
        for j in range(N):
            x = rng.uniform(low=-R - d, high=R * 2 + d)
            y = rng.uniform(low=-R - d, high=R + d)
            p.append(fp(x, y, R))

        Pst = sum(p) / N
        v = f"Геометрическая вероятность = {PT}, Статистическая вероятность = {Pst}"
        file.writelines(v + '\n')