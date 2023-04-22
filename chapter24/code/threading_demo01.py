from threading import Thread
import time

url_list = [
    'https://www.baidu.com',
    'https://www.zhihu.com',
    'https://www.163.com',
]


class MyThread(Thread):

    def __init__(self, url):
        self.url = url
        super(MyThread, self).__init__()  # 父类初始化变量

    def run(self):
        """
        线程必须运行的线程体
        :return:
        """
        time.sleep(1)
        print(self.url, time.ctime())


if __name__ == '__main__':
    t_list = []
    for url in url_list:
        t = MyThread(url)
        t.start()

    [t.join() for t in t_list]
