# def f1():
#     def f2():
#         pass
import time


def f1():
    time.sleep(1)
    print("函数执行完毕！")


def outer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("执行时间：", end_time - start_time)


outer(f1) # 调用方式变了  f1()
