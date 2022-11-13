def wrapper(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return inner


@wrapper
def f1(a, b):
    return a + b


res = f1(1, 2)

print(res)  # None
