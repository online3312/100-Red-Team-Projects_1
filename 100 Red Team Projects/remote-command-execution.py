import socket
import subprocess
import threading

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    while True:
        try:
            command = conn.recv(1024).decode()
            if not command:
                break
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            conn.send(output.stdout.encode() + output.stderr.encode())
        except:
            conn.close()
            break

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
