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