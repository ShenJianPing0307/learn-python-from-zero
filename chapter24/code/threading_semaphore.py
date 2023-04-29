import threading
import time


def check_person(i, sem):
    sem.acquire()
    print("检查{}".format(i), time.ctime())
    time.sleep(1)
    sem.release()


if __name__ == '__main__':
    sem = threading.Semaphore(4)  # 同时四个人进行检查

    for i in range(50):
        t = threading.Thread(target=check_person, args=(i, sem))
        t.start()
