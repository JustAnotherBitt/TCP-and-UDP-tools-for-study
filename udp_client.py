import socket
target_host = "127.0.0.1"
target_port = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET = IPv4 // SOCK_DGRAM = indicates that this will be a UDP client
# send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))
# receive some data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()
