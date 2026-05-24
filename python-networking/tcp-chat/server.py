import socket

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

conn, addr = server.accept()

print(f"[NEW CONNECTION] {addr} connected.")

while True:
    try:
        message = conn.recv(1024)

        if not message:
            print(f"[DISCONNECTED] {addr} Client disconnected.")
            break

        decoded_message = message.decode()
        print(f"[{addr}]: {decoded_message}")

        reply = input("[YOU]: ")
        conn.send(reply.encode())

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        break

conn.close()
print("[CLOSED] Connection closed.")
server.close()
print("[SHUTDOWN] Server shutdown.")