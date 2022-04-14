import socket
import sys

my_socket = socket.socket()
args = sys.argv
ip = args[1]
port = int(args[2])
data = args[3].encode()

my_socket.connect((ip, port))
my_socket.send(data)
response = my_socket.recv(1024).decode()
print(response)
my_socket.close()
