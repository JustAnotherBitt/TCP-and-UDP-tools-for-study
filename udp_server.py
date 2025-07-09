# udp_server.py
import socket

ip = "127.0.0.1"
port = 9997

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))
print(f"[*] UDP server listening at {ip}:{port}")

while True:
    data, addr = server.recvfrom(4096)
    print(f"Received from {addr}: {data.decode()}")
    server.sendto(b"Successfully received", addr)
