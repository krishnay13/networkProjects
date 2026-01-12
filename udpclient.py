import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345

s.sendto(bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "utf-8"), (host, port))
print(s.recvfrom(1024)[0].decode('utf-8'))
s.close()