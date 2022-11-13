# def f1():
#     def f2():
#         pass
import time


def outer(func):
    print("开始执行outer")

    def inner1():
        print("outer")
        start_time = time.time()
        func()
        end_time = time.time()
        print("执行时间：", end_time - start_time)

    return inner1


def wrapper(func):
    print("开始执行wrapper")

    def inner2():
        func()
        print("wrapper")

    return inner2


@wrapper
@outer  # inner1   --> wrapper(inner1) 没有执行inner1 --> inner2   # wrapper(outer(func))
def f1():
    time.sleep(1)
    print("函数执行完毕！")


"""
"开始执行outer"
"开始执行wrapper"
"outer"
"函数执行完毕！"
执行时间：1.0221
"wrapper"
"""

# f1 = outer(f1)
f1()

# @outer
# def f2():
#     pass

# outer(f1)() # 调用方式变了  f1()

# f1 = outer(f1)
# f1()
# @outer 相当于 f1= outer(f1)

# f1()
