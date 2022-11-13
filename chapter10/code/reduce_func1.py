l1 = [i for i in range(100)]


def func(iterable, initial=None):
    sum = 0
    if initial:
        sum = initial

    for i in iterable:
        sum += i

    return sum


def reduce(func, iterable, initial=None):
    return func(iterable, initial)


res = reduce(func, l1, 1000)
print(res)
