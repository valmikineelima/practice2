import socket

def start_client():
    host = '127.0.0.1'  # Loopback address
    port = 12345         # Port to connect to

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        # Send a message to the server
        message = input("Enter your message (type 'bye' to exit): ")
        client_socket.send(message.encode('utf-8'))

        # Check if the client wants to terminate
        if message.lower() == 'bye':
            print("Terminating client program.")
            break

        # Receive and print the server's response
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()