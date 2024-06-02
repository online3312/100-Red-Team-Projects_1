import socket

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

# 클라이언트 리스트
clients = []

# 서버 실행
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Server started")
    while True:
        message, addr = server.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            if client != addr:
                server.sendto(message, client)

if __name__ == "__main__":
    main()
