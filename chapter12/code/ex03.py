def example_exception():
    a = 1
    b = 0
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


def example_exception1():
    try:
        a = 1
        b = 0
        if b == 0:
            raise ZeroDivisionError("除数不能为0")
        return a / b
    except ZeroDivisionError as e:
        print(e)


example_exception1()
