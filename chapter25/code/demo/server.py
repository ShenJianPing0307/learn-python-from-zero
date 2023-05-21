import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    break
                print("收到的消息：", data)
                # 发消息
                self.request.sendall(data.upper())
            except Exception as e:
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8001), MyServer)
    server.serve_forever()
