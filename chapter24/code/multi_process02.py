from multiprocessing import Process
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
    for url in url_list:
        handle_task(url)
    end_time = time.time()
    print(end_time-start_time)
