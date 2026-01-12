import socket
import threading
import time

def run_client(client_id):
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    time.sleep(5)
    data = s.recv(1024)
    print(f"Client {client_id} received: {data.decode('utf-8')}")
    time.sleep(5)
    s.close()

threads = []
for i in range(2):
    t = threading.Thread(target=run_client, args=(i+1,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
