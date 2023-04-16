from concurrent.futures import ProcessPoolExecutor
import time


def task(task):
    time.sleep(1)
    print(task, time.ctime())



url_list = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]
if __name__ == '__main__':
    pool = ProcessPoolExecutor(2)
    for url in url_list:
        pool.submit(task, url)  # 相当于apply_async()异步方法
    pool.shutdown()  # 相当于close和join方法
