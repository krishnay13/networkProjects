import socket
import datetime
import threading

MAX_CONNECTIONS = 3 
TIMEOUT = 20  

def handle_client(c, addr):
    print(f"Got a connection from {addr}")
    c.send(bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "utf-8"))
    c.close()

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(5)
s.settimeout(TIMEOUT) 

connection_count = 0
try:
    while connection_count < MAX_CONNECTIONS:
        try:
            c, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(c, addr))
            t.start()
            connection_count += 1
        except socket.timeout:
            print(f"No connections received in {TIMEOUT} seconds. Server is timing out.")
            break
finally:
    s.close()