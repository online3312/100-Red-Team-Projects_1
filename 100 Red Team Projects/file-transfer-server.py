import socket
import threading

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

# 클라이언트 처리
def handle_client(conn, addr):
    print(f"New connection: {addr}")
    filename = conn.recv(1024).decode()
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    conn.close()
    print(f"File {filename} received from {addr}")

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
