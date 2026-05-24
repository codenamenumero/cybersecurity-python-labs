import socket

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    try:
        message = input("[YOU]: ")
        if message.lower() == 'exit':
            print("[DISCONNECTING] Disconnecting from server.")
            break

        client.send(message.encode())

        reply = client.recv(1024)
        decoded_reply = reply.decode()

        print(f"[SERVER]: {decoded_reply}")

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        break

client.close()
print("[CLOSED] Connection closed.")