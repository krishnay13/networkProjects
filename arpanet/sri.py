import socket

HOST = 'localhost'
PORT = 1969

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

for i in range(10):
    data = conn.recv(1).decode()
    print(f"[SRI] Received: {data}")
    if(i >= 2):
        conn.send(b"CRASH")
        break
    else:
        conn.send(b"OK")



conn.close()
s.close()