import socket
import datetime

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print(f"Got a connection from {addr}")
    c.send(bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "utf-8"))
    c.close()
    break
s.close()