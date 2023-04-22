from concurrent.futures import ThreadPoolExecutor
import requests
import time


def task(url):
    response = requests.get(url)
    return response


# ########d###
def done(future, *args, **kwargs):
    """
    done为回调函数，task执行的结果返回给future,将结果与之后的动作分离开来

    :param future:
    :param args:
    :param kwargs:
    :return:
    """
    response = future.result()
    print(response.text)


pool = ThreadPoolExecutor(5)

url_list = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]
for url in url_list:
    res = pool.submit(task, url)
    res.add_done_callback(done)

pool.shutdown()