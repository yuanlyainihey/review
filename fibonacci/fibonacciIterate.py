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