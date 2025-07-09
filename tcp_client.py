import socket

target_host = "0.0.0.0" # change it for some host such as www.google.com for further testing
target_port = 9998 # hange it for the default port for web (80) for further testing

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 // SOCK_STREAM = indicates that this will be a TCP client
# connect the client
client.connect((target_host,target_port))
# send some data
client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
# receive some data

response = client.recv(4096)
print(response.decode())
client.close()
