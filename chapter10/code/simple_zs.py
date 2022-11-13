import time


# def f1():
#     time.sleep(1)
#     print("函数执行完毕！")
#
#
# f1()

def f1():
    start_time = time.time()
    time.sleep(1)
    print("函数执行完毕！")
    end_time = time.time()
    print("执行时间：",end_time-start_time)


f1()

