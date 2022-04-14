import socket
import sys
from itertools import product
import json

args = sys.argv
host = (args[1], int(args[2]))
buffer = 1024

fail_login = 'Wrong login!'
success_msg = 'Connection success!'; response = ''; found = False

with socket.socket() as my_socket:
    my_socket.connect(host)

    with open('logins.txt', 'r') as logs:
        dummy_gen = (line.strip() for line in logs.readlines())
        while response == fail_login:
            guess = next(dummy_gen)
            context = {
                'admin': guess,
                'password': ' '
            }
            my_socket.send(json.dumps(context))
            response = my_socket.recv(buffer).decode()

    with open('passwords.txt', 'r') as pws:
        dummy_gen = (line.strip() for line in pws.readlines())
        for dummy in dummy_gen:
            opt_gen = product(*((char.lower(), char.upper()) if not char.isnumeric()
                                else char for char in dummy))
            for opt in opt_gen:
                opt = ''.join(opt)
                my_socket.send(opt.encode())
                response = my_socket.recv(buffer).decode()
                if response == success_msg:
                    found = True
                    break
            if found:
                break
    print(opt)
