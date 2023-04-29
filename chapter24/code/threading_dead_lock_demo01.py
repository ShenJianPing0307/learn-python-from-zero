import threading, time

def eat1(name):
    noodle_lock.acquire()
    time.sleep(3)
    print("%s获取面条"%name)
    fork_lock.acquire()
    print("%s获取叉子" % name)
    print("%s吃面" % name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    time.sleep(5)
    print("%s获取叉子"%name)
    noodle_lock.acquire()
    print("%s获取面条" % name)
    print("%s吃面" % name)
    noodle_lock.release()
    fork_lock.release()

if __name__ == '__main__':
    noodle_lock = threading.Lock()
    fork_lock = threading.Lock()

    threading.Thread(target=eat1, args=('zs',)).start()
    threading.Thread(target=eat2, args=('ls',)).start()