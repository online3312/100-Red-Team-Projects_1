import socket
import sys
import threading

def handle_receive(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode(), end='')

def main():
    if len(sys.argv) < 4:
        print("Usage: python netcat.py <mode> <host> <port>")
        sys.exit(1)

    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])

    if mode == 'listen':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print(f"Listening on {host}:{port}")
        conn, addr = server.accept()
        print(f"Connection from {addr}")

        thread = threading.Thread(target=handle_receive, args=(conn,))
        thread.start()

        while True:
            message = input()
            if not message:
                break
            conn.send(message.encode())

    elif mode == 'connect':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        thread = threading.Thread(target=handle_receive, args=(client,))
        thread.start()

        while True:
            message = input()
            if not message:
                break
            client.send(message.encode())

    else:
        print("Invalid mode. Use 'listen' or 'connect'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
