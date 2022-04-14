import socket
import sys
from string import ascii_lowercase, digits
from itertools import product


args = sys.argv
host = (args[1], int(args[2]))
buffer = 1024

char_base = ''.join((ascii_lowercase, digits))
pw_gen = (comb for i in range(1, len(char_base) + 1) for comb in product(char_base, repeat=i))
success_msg = 'Connection success!'; response = ''

with socket.socket() as my_socket:
    my_socket.connect(host)
    while response != success_msg:
        pw = ''.join(next(pw_gen))
        my_socket.send(pw.encode())
        response = my_socket.recv(buffer).decode()
    print(pw)
