import numpy as np


def fibonacciMatrix(n):         # 矩阵
    result = []
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        result.append(int(res[0][0]))
    return result