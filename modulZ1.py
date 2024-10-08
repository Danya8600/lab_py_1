import numpy as np


def fp(x, y, R=10.):
    D1 = (x >= 0 and y >= 0) and (x <= R * 2) and ((x - R) ** 2 + y ** 2 <= R ** 2)
    D2 = (x <= 0 and y <= 0) and (x >= -R and y >= -R) and ((-R - x) ** 2 + (-R - y) ** 2 >= R ** 2)
    return D1 or D2


def P_Geometry(R):
    SD = ((np.pi * (R ** 2)) * (180 / 360)) + (R ** 2 - ((np.pi * (R ** 2)) * (90 / 360)))
    d = R / 30
    x_min = - R - d
    x_max = R + d
    y_min = - R - d
    y_max = R - d
    S0 = (x_max - x_min) * (y_max - y_min)
    return SD / S0
