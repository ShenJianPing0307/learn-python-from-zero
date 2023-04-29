from threading import Thread, current_thread


def handle():
    x = 1
    for _ in range(50):
        x += 1
    print(current_thread(), x)


if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=handle)
        t.start()
