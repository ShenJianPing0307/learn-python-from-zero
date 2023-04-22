import multiprocessing

data = 100


def task():
    global data
    data -= 1


if __name__ == '__main__':
    p_list = []

    for i in range(10):
        p = multiprocessing.Process(target=task)
        p_list.append(p)
        p.start()

    for j in p_list:
        j.join()

    print(data)
