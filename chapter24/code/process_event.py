# from multiprocessing import Process, Event
# import random, time
#
#
# def light(e):
#     """
#     e.is_set() 判断当前的Flag的值 False 、True
#     e.clear() Flag的值改成False、阻塞
#     e.set() 将Flag改为True，解除阻塞
#     :param e:
#     :return:
#     """
#     while True:
#         if e.is_set():  # True 绿灯
#             e.clear()  # 将绿灯变成红灯
#             print("红灯亮了")
#         else:
#             e.set()
#             print("绿灯亮了")
#
#
# def cars(e, i):
#     if not e.is_set():
#         print("{}车等待在十字路口".format(i))
#         e.wait()  # 阻塞, 直到Flag变成True
#     else:
#         print("{}车通过十字路口".format(i))
#
#
# if __name__ == '__main__':
#
#     e = Event()  # 实例化一个事件
#     l = Process(target=light, args=(e,))  # 红绿灯进程
#     l.start()
#
#     car_list = []
#
#     for i in range(10):
#         time.sleep(random.random())
#         car = Process(target=cars, args=(e, i))
#         car.start()
#         car_list.append(car)
#
#     [car.join() for car in car_list]

import threading
import time

def cars(e,i):
    if not e.is_set():
        print("%s车等待在十字路口"%i)
        e.wait()  #阻塞，直到flag变成True
    else:
        print("%s车通过了十字路口"%i)

def light(e):
    while True:
        if e.is_set():#绿灯
            e.clear() #将flag改为False,进程阻塞，
            print("红灯亮了")
        else: #默认走else,因为默认flag是False
            e.set() #将flag改为True,此时执行car进程，绿灯车通过
            print("绿灯亮了")
            time.sleep(3) #wait没有阻塞，汽车通行

if __name__ == '__main__':
    e = threading.Event() #默认为False,红灯亮
    t = threading.Thread(target=light,args=(e,)) #红绿灯线程
    t.start() #启动红绿灯线程

    car_list = []
    for i in range(10): #10辆车过红绿灯
        time.sleep(1)
        car = threading.Thread(target=cars,args=(e,i,))
        car.start()
        car_list.append(car)
    [car.join() for car in car_list]