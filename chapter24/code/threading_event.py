import threading
import time


def light(e):
    """更改红绿灯"""
    while True:
        if e.is_set():  # 是绿灯
            e.clear()
            print("红灯亮了！")
        else:
            e.set()  # 更改绿灯 flag = True
            print("绿灯亮了！")
            time.sleep(0.2)


def cars(e, i):
    """具体的车, 根据event的状态来进行停车或者行走"""
    if e.is_set:
        print("%s车过马路了" % i)
    else:
        print("%s车等在十字路口" % i)
        e.wait()  # 阻塞, 直到 flag=True


if __name__ == '__main__':
    e = threading.Event()  # 默认为False,红灯

    t = threading.Thread(target=light, args=(e,))
    t.start()  # 启动一个红绿灯的线程

    car_list = []
    for i in range(10):
        car = threading.Thread(target=cars, args=(e, i))
        car_list.append(car)
        car.start()

    [car.join() for car in car_list]
    t.join()
