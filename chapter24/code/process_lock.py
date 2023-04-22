from threading import Lock, Thread

data = 100  # 设置一个共享的全局变量


def handle(lock):
    global data
    lock.acquire()  # 拿到钥匙
    data = data - 1
    lock.release()  # 归还钥匙


if __name__ == '__main__':
    lock = Lock()

    t_list = []
    for i in range(5):
        t = Thread(target=handle, args=(lock,))
        t_list.append(t)
        t.start()

    [t.join() for t in t_list]  # 等待所有的线程执行完毕

    print(data)