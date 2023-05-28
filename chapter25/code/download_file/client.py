import socket


def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(("127.0.0.1", 5000))

    recv_data = tcp_client.recv(1024)

    if recv_data:
        with open("test_socket1.txt", "wb") as f:
            f.write(recv_data)

    tcp_client.close()


if __name__ == '__main__':
    main()
