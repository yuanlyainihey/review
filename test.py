import numpy as np
import pandas as pd


def solution(n):
    l = len(n)
    if l == 1:
        print(1, 1)
        return
    matrix = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            matrix[i][j] = sum(n[i][:]) + sum(n[:][j]) - n[i][j]
    tmp = pd.DataFrame(matrix)
    idmax = tmp.stack().idxmax()
    print(idmax[0]+1, idmax[1]+1)
    arr = np.delete(n, idmax[1], axis=1)
    arr2 = np.delete(arr, idmax[0], axis=0)
    solution(arr2)

if __name__ == '__main__':
    matrixSize = int(input())
    matrix = []
    for i in range(matrixSize):
        row = list(map(int, input().split()))
        matrix.append(row)
    solution(matrix)