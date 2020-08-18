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