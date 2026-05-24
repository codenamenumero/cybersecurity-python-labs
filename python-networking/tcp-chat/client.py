import socket
from datetime import datetime
from colorama import Fore, init, Style

init(autoreset=True)


HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

USERNAME = input("Enter your username: ")
client.send(USERNAME.encode())

while True:
    try:
        message = input(Fore.GREEN + "[YOU]: ")
        if message.lower() == 'exit':
            print(Fore.RED + "[DISCONNECTING] Disconnecting from server.")
            break

        client.send(message.encode())

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        reply = client.recv(1024).decode()

        print(Fore.MAGENTA + f"[{current_time}] [SERVER]: {reply}")

    except Exception as e:
        print(Fore.RED + f"[ERROR] An error occurred: {e}")
        break

client.close()
print("[CLOSED] Connection closed.")