import socket

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ensure that you can restart your server quickly when it terminates
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set the client socket's TCP "well-known port" number
port = 3600
sock.bind(('', port))

# Set the number of clients waiting for connection that can be queued
sock.listen(5)

# loop waiting for connections (terminate with Ctrl-C)
try:
    while 1:
        socket, address = sock.accept()
        print("Connected from", address)
        # loop serving the new client
        while 1:
            data = socket.recv(1024)

            if not data: 
                break
            # Echo back the same data you just received
            socket.send(data)

        socket.close()
        print("Disconnected from", address)

finally:
    sock.close()
