#include <stdio.h>
#include <winsock2.h>
#pragma comment(lib, "ws2_32.lib")

#define HOST "127.0.0.1"
#define PORT 1969

int main(){
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);

    SOCKET s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = inet_addr(HOST);

    //python equivalent -> s.connect((HOST, PORT))
    connect(s, (struct sockaddr*)&addr, sizeof(addr));

    char buf[6];
    char *message = "LOGIN";
    for(int i = 0; message[i] != '\0'; i++){
        send(s, &message[i],1,0);
        int n = recv(s, buf, 5, 0);
        buf[n] = '\0';
        printf("[UCLA] SRI says: %s\n", buf);
        if (buf[0] == 'C') break;
    }
    closesocket(s);
    WSACleanup();

    return 0;
}