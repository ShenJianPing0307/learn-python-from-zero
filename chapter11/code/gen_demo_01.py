"""
0 1 1 2 3...
"""


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield a
        a, b = b, a + b
        n += 1


f = fib(10)

for i in f:
    print(i)
