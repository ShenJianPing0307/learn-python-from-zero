from concurrent.futures import ThreadPoolExecutor
import requests
import time


def task(url):

    response=requests.get(url)
    print(response,time.ctime())


pool=ThreadPoolExecutor(5)

url_list=[
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]
for url in url_list:
    pool.submit(task,url) #异步提交任务

pool.shutdown() #相当于进程池的pool.close()+pool.join()操作
