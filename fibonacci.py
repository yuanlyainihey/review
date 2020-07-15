def fibonacciRecursive(n):      # 递归
    if n <= 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


def fibonacciIterate(n):        # 迭代
    if n <= 0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fibonacciRecursive(5))
    print(fibonacciIterate(5))