x = 5


def outer():
    x = 10

    def foo():
        nonlocal x  # 指定上一级的变量（非全局变量），如果没有就继续往常查找，知道找到为止
        print(x)

    return foo


outer()()
