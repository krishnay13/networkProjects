import socket

HOST = 'localhost'
PORT = 1969

# (We'll build this after SRI is working)
s = socket.socket()
s.connect((HOST, PORT))

for char in "LOGIN":
    s.send(char.encode())
    response = s.recv(1024).decode()
    print(f"[UCLA] Received: {response}")
    if response == "CRASH":
        break

s.close()