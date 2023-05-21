import socket

# 1、创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、连接服务器
client.connect(("127.0.0.1", 8000))

# 3、发送消息
client.send(b"hello world!") # bytes("hello world!")

# 4、接收消息
data = client.recv(1024)
print("服务端发送的数据是：", data)

# 关闭套接字
client.close()