import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345

s.bind((host, port))

while True:
    data, addr = s.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode('utf-8')}")
    s.sendto(bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "utf-8"), addr)
    break
s.close()

