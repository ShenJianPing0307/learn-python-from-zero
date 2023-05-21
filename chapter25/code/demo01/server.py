import socket

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
conn, addr = server.accept()
print(type(conn), type(addr))
# 5、接收客户端消息
msg = conn.recv(1024) # 接收消息
print("客户端发来的消息：", msg)
# 6、发送消息给客户端
conn.send(msg.upper())

# 7、关闭连接和server
conn.close()
server.close()
