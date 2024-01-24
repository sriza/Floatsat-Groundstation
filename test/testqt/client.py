import socket
import os


# 
# HOST = "127.0.0.1"  # The server's hostname or IP address
# HOST = "255.255.255.255"  # The server's hostname or IP address
# HOST = "1"  # The server's hostname or IP address
HOST =  "192.168.137.36"
PORT = 50000  # The port used by the server


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    while True:
        print("here")
        data, addr =sock.recvfrom(1024)
        print("message:", data)
        print("hi")
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #     s.connect((HOST, PORT))
    #     # s.sendall(b"Hello, world")
    #     data = s.recv(1024)

    print(f"Received {data!r}")
except Exception as e:
    print(e)
    