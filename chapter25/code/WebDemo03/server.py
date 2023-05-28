import socket

server = socket.socket()

server.bind(("127.0.0.1", 5001))

server.listen()

while True:
    # 等待客户端访问
    client, addr = server.accept()
    # 接收数据
    data = client.recv(1024)
    print("data",data)
    # 状态行
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # 响应体
    with open("index.html", mode="rb") as f:
        response = f.read()
    client.send(response)
    client.close()


