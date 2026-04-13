#include <stdio.h>
#include <winsock2.h>
#pragma comment(lib, "ws2_32.lib")

#define PORT 1969

int main() {
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);

    // python equivalent -> s=socket.socket()
    SOCKET s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = INADDR_ANY;


    // python equivalent -> s.bind((HOST, PORT))
    bind(s, (struct sockaddr*)&addr, sizeof(addr)); 

    // python equivalent -> s.listen(1)
    listen(s, 1);

    // python equivalent -> conn, addr = s.accept()
    SOCKET conn = accept(s, NULL, NULL);

    
    // python equivalent -> data = conn.recv(1) loop
    char buf[2];
    buf[1] = '\0';
    for (int i = 0; i < 10; i++){
        recv(conn, buf, 1, 0);
        printf("[SRI] Got: %s\n", buf);
        if(i >= 2){
            send(conn, "CRASH", 5, 0);
            break;
        }
        else{
            send(conn, "OK", 2, 0);
        }
    }

    closesocket(conn);
    closesocket(s);
    WSACleanup();
    
    return 0;
}
