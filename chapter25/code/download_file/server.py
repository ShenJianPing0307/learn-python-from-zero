import socket


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("127.0.0.1", 5000))
    tcp_server.listen()
    client, addr = tcp_server.accept()

    with open("./test_socket.txt", "rb") as f:
        file_content = f.read()
        f.close()

    client.send(file_content)

    client.close()
    tcp_server.close()


if __name__ == '__main__':
    main()
