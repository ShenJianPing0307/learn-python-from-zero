from multiprocessing import Pool
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

    p_list = []

    p = Pool(2)

    for url in url_list:
        p.apply_async(handle_task, args=(url,))
        p_list.append(p)
    print('waiting for all subprocesses done...')
    p.close()  # 关闭进程池

    # 等待所有的子进程结束，再结束主进程
    for p in p_list:
        p.join()

    print('all processes done...')
