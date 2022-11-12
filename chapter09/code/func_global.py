x = 10


def foo():
    global x  # 引入定义的全局变量
    x = 20


foo()

print(x)  # 20
