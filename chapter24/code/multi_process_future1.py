from concurrent.futures import ProcessPoolExecutor
import time


def task(task):
    return task

def done_res(future, *args, **kwargs):
    print('future', future)
    print(future.result())

url_list = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]
if __name__ == '__main__':
    pool = ProcessPoolExecutor(2)
    for url in url_list:
        res = pool.submit(task, url)  # 相当于apply_async()异步方法
        res.add_done_callback(done_res) # 将接收的值 future 传入回调函数
    pool.shutdown()  # 相当于close和join方法
