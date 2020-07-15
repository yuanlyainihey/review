def fibonacciRecursive(n):  # 递归
    if n <= 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


dict_fib = {}


def fibonacciRecursiveRecord(n):        # 递归 加记录
    if n <= 2:
        return 1
    elif dict_fib.get(n):
        return dict_fib.get(n)
    else:
        dict_fib[n] = fibonacciRecursiveRecord(n-1) + fibonacciRecursiveRecord(n-2)
        return dict_fib[n]


def fibonacciIterateFor(n):  # 迭代
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def fibonacciIterateWhile(n):  # 迭代
    if n <= 0:
        return 0
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fibonacciYieldFor(n):  # 生成器
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def fibonacciYieldWhile(n):  # 生成器
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


class Fibonacci(object):  # 类内部实现-迭代器

    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


import numpy as np


def fibonacciMatrix(n):         # 矩阵
    result = []
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        result.append(int(res[0][0]))
    return result


if __name__ == '__main__':
    num = 10
    # for i in range(1, num+1):
    #     print(fibonacciRecursive(i))
    print(fibonacciRecursiveRecord(num))
    print(dict_fib)
    # for i in range(1, num+1):
    #     print(fibonacciIterateFor(i))
    # for i in range(1, num + 1):
    #     print(fibonacciIterateWhile(i))
    # for i in fibonacciYieldFor(num):
    #     print(i)
    # for i in fibonacciYieldWhile(num):
    #     print(i)
    # fibonacci = Fibonacci(num)
    # for fibNum in fibonacci:
    #     print(fibNum)
    # print(fibonacciMatrix(num))