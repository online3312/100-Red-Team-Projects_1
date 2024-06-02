import socket
import threading

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

# 클라이언트 리스트
clients = []

# 클라이언트로 메시지 전송
def broadcast(message, conn):
    for client in clients:
        if client != conn:
            client.send(message)

# 클라이언트 처리
def handle_client(conn, addr):
    print(f"New connection: {addr}")
    clients.append(conn)
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            broadcast(message, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

# 서버 실행
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Server started")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
