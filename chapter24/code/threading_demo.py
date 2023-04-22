from threading import Thread
from os import cpu_count
import time

url_list = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]

def handle_task(task):
    time.sleep(1)
    print(task, time.ctime())

if __name__ == '__main__':
    start_time = time.time()
    t_list = []
    for url in url_list:
        t = Thread(target=handle_task, args=(url,))
        t_list.append(p)
        t.start()

    for t in t_list:
        t.join() # 子进程执行结束后才能结束主进程

    end_time = time.time()
    print(end_time-start_time)