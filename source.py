import socket
import random

# Define the server host and port
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print('Server listening on {}:{}'.format(host, port))

# Accept a client connection
client_socket, addr = server_socket.accept()
print('Connected to client:', addr)

# Prompt for the file name and read its contents
file_name = input('Enter the file name: ')

try:
    # Read the contents of the file
    with open(file_name, 'r') as file:
        file_contents = file.read()
    print('File read successfully.')

    # Break down the file contents into chunks of 5 characters
    chunk_size = 5
    chunks = [file_contents[i:i+chunk_size] for i in range(0, len(file_contents), chunk_size)]

    # Generate random order for the chunks
    random_order = list(range(1, len(chunks) + 1))
    random.shuffle(random_order)

    # Display the shuffled chunks with assigned numbers
    for i, chunk_num in enumerate(random_order):
        print('[{}] {}'.format(chunk_num, chunks[i]))

    # Send the shuffled chunks and random order to the client
    chunks_with_order = [(chunk_num, chunks[i]) for i, chunk_num in enumerate(random_order)]
    client_socket.sendall(str(chunks_with_order).encode())
    print('Shuffled chunks and order sent to client.')

except FileNotFoundError:
    print('File not found.')

# Close the connection
client_socket.close()
server_socket.close()
