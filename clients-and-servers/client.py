import socket
 
# Create a connection to the server application on port 81
tcp_socket = socket.create_connection(('localhost', 81))
 
try:
    while True:
        data = input("say something: ")
        if data == 'X':
            break
        else:
            data = str.encode(data)
            tcp_socket.sendall(data)
        while True:
            chunk = tcp_socket.recv(1024)
            print(chunk)
            if not chunk:
                break
 
finally:
    print("Closing socket")
    tcp_socket.close()