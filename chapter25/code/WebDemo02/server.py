import socket

server = socket.socket()

server.bind(("127.0.0.1", 5001))

server.listen()

# 视图函数，主要做业务
def index():

    return b"index"

def home():

    return b"home"

# 路由
urlpattern = [
    ("/index.html", index),
    ("/home.html", home)
]

while True:
    # 等待客户端访问
    client, addr = server.accept()
    # 接收数据
    data = client.recv(1024)
    data = str(data, encoding="utf8")
    url = data.split("\r\n")[0].split()[1]

    func = None
    for path_tuple in urlpattern:
        if path_tuple[0] == url:
            func = path_tuple[1]
            break
    if func:
        response = func()
    else:
        response = b"404 not found..."
    # 状态行
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # 响应体
    client.send(response)
    client.close()


