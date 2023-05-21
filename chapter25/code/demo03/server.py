import socket
import threading


def handle_client(conn, addr):
    # 5、接收客户端消息
    while True:
        try:
            msg = conn.recv(1024)  # 接收消息
            if msg:
                print("客户端发来的消息：", msg)
                # 6、发送消息给客户端
                conn.send(msg.upper())
            else:
                print("client disconnected!")
        except Exception as e:
            conn.close()
# socket也被叫做套接字
# family 用途
# type 数据传输的方式
# 1、创建本地套接字
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 2、绑定具体的应用, ip:port
server.bind(('127.0.0.1', 8000))

# 3、监听
server.listen()

# 4、等待客户端连接,阻塞
while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()

