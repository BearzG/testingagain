import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 80))

s.listen(3)

while True:
    s_client, ip = s.accept()
    s_client.send(bytes("You are connection to a server e.e", 'utf-8'))
