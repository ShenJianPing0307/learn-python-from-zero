def wrapper(func):
    def inner(*args, **kwargs):  # args (1, 2)
        func(*args, **kwargs)  # func(args[0],args[1])

    return inner


@wrapper  # f1 = inner(*args, **kwargs)
def f1(a, b):
    print(a + b)


f1(1, 2)
