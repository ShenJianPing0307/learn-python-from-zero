import multiprocessing
import os


def handle_message(conn):
    conn.send('I am child_conn')
    res = conn.recv()
    print("child_conn", res, os.getpid())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    # 启动child进程
    p = multiprocessing.Process(target=handle_message, args=(child_conn,))
    p.start()

    res = parent_conn.recv()
    print('parent_res', res)

    parent_conn.send("I am parent_conn")
    p.join()
