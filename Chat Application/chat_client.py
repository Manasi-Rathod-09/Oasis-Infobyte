import socket

def start_client():
    host = '127.0.0.1'  # Server's address
    port = 12345        # Port to connect to

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}.")

    while True:
        # Send a message to the server
        client_message = input("You: ")
        client_socket.send(client_message.encode('utf-8'))
        if client_message.lower() == 'exit':
            print("You left the chat.")
            break

        # Receive message from the server
        server_message = client_socket.recv(1024).decode('utf-8')
        if server_message.lower() == 'exit':
            print("Server has ended the chat.")
            break
        print(f"Server: {server_message}")

    client_socket.close()
    print("Client disconnected.")

if __name__ == "__main__":
    start_client()
