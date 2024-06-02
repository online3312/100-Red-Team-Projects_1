import socket
import threading

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

# 클라이언트 리스트
clients = []

def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def broadcast(message, conn):
    for client in clients:
        if client != conn:
            client.send(message)

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    clients.append(conn)
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            encrypted_message = caesar_cipher(message.decode(), 3).encode()
            broadcast(encrypted_message, conn)
        except:
            clients.remove(conn)
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
