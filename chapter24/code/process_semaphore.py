from multiprocessing import Semaphore, Process
import time, random


def check_person(sem, i):
    sem.acquire()  # 控制4个进程，同时有4把钥匙
    print("%s走进监察室" % i, time.ctime())
    time.sleep(random.uniform(0, 1))
    print("%s检查完毕" % i, time.ctime())
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)  # 信号量，同时可以处理4个进程

    p_list = []
    for i in range(9):
        p = Process(target=check_person, args=(sem, i))
        p.start()
        p_list.append(p)

    for j in p_list:
        j.join()
