import multiprocessing
import time


def handle_message(q, i):
    time.sleep(0.1)
    q.put(i)


if __name__ == '__main__':

    q = multiprocessing.Queue()

    p_list = []

    for i in range(10):
        p = multiprocessing.Process(target=handle_message, args=(q, i))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print(q.get())
    print(q.get())