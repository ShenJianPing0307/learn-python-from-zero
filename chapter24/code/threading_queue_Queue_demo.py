import queue
import threading
import time


def do_work(item):
    print("%s任务已经完成" % item)
    time.sleep(0.2)


def worker():
    """每一个线程"""
    while True:
        item = q.get()
        if item is None:
            break
        # 处理任务的具体逻辑
        do_work(item)
        q.task_done()  # 任务完成后向队列发送一个通知信号


if __name__ == '__main__':
    q = queue.Queue()  # 实例化一个 先进先出 队列
    t_list = []
    num_worker_threads = 5

    # 将10个任务放入到队列中
    for item in range(10):
        q.put(item)

    # 5个工作线程处理任务
    for _ in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        t_list.append(t)

    # 等待队列中所有任务全部取出并且进行处理
    q.join()

    # 等待所有的工作线程结束
    for _ in range(num_worker_threads):
        q.put(None)

    [t.join() for t in t_list]
