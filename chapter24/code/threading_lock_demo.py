from threading import Thread, Lock

x = 100


def handle(lock):
    global x
    lock.acquire()  # 拿到钥匙
    x -= 1
    lock.release()  # 归还钥匙


if __name__ == '__main__':
    lock = Lock()

    t_list = []
    for i in range(5):
        t = Thread(target=handle, args=(lock,))
        t_list.append(t)
        t.start()
    [t.join() for t in t_list]

    print(x)
