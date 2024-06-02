import socket

# 서버 설정
HOST = '127.0.0.1'
PORT = 12345

# 클라이언트 리스트
clients = []

def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Server started")
    while True:
        message, addr = server.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        encoded_message = rot13(message.decode()).encode()
        for client in clients:
            if client != addr:
                server.sendto(encoded_message, client)

if __name__ == "__main__":
    main()
