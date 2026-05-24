import socket
from datetime import datetime
from colorama import Fore, init, Style

init(autoreset=True)

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(Fore.GREEN + f"[LISTENING] Server is listening on {HOST}:{PORT}")

conn, addr = server.accept()

print(Fore.CYAN + f"[NEW CONNECTION] {addr} connected.")

username = conn.recv(1024).decode()

print (Fore.YELLOW + f"[USERNAME] {username} joined the chat.")

while True:
    try:
        message = conn.recv(1024)

        if not message:
            print(Fore.RED + f"[DISCONNECTED] {addr} Client disconnected.")
            break

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        decoded_message = message.decode()
        print(Fore.BLUE + f"[{current_time}] {username}: {decoded_message}")

        reply = input(Fore.GREEN + "[SERVER]: ")
        conn.send(reply.encode())

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        break

conn.close()
print(Fore.RED + "[CLOSED] Connection closed.")
server.close()
print(Fore.RED + "[SHUTDOWN] Server shutdown.")