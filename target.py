import socket
import ast
import threading

# Define the server host and port
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))
print('Connected to server {}:{}'.format(host, port))

# Receive the shuffled chunks and order from the server
chunks_with_order = ast.literal_eval(client_socket.recv(4096).decode())

# Rearrange the chunks in the correct order based on chunk_num
ordered_chunks = [chunk for chunk_num, chunk in sorted(chunks_with_order, key=lambda x: x[0])]

# Define a thread function to display the ordered chunks
def display_ordered_chunks():
    print('\nOrdered chunks (correct order):')
    print(' '.join(ordered_chunks))

# Start a new thread to display the ordered chunks
thread = threading.Thread(target=display_ordered_chunks)
thread.start()

# Wait for the thread to complete
thread.join()

# Close the connection
client_socket.close()
