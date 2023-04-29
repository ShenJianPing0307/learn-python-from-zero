from threading import local, Thread, current_thread

data = local()  # 定义一个全局的local对象

print(data, type(data))


def handle():
    data.x = 1

    for i in range(50):
        data.x += 1
    print(current_thread(), data.x)


if __name__ == '__main__':

    for i in range(5):
        t = Thread(target=handle)
        t.start()
