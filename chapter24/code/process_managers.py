from multiprocessing import Manager,Process
import os

def handle_message(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() #生成一个字典，可在多个进程间共享、传递
        l = manager.list() #生成一个列表，可在多个进程间共享、传递

        p_list = []
        for i in range(3):
            p = Process(target=handle_message,args=(d,l))
            p.start()
            p_list.append(p)

        for j in p_list: #等待子进程结果
            j.join()

        print(d)
        print(l)