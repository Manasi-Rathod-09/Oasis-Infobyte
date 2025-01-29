import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to bind to

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for 1 connection at a time

    print(f"Server started. Waiting for a connection on {host}:{port}...")

    # Accept connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Receive message from the client
        client_message = conn.recv(1024).decode('utf-8')
        if client_message.lower() == 'exit':
            print("Client has left the chat.")
            break
        print(f"Client: {client_message}")

        # Send a message to the client
        server_message = input("You: ")
        conn.send(server_message.encode('utf-8'))
        if server_message.lower() == 'exit':
            print("You left the chat.")
            break

    conn.close()
    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    start_server()
