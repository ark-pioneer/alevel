import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('localhost', 81))
tcp_socket.bind(server_address)

tcp_socket.listen(5)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
 
    try:
        print("Connected to client IP: {}".format(client))
         
        # Receive and 1024 bytes at a time, as long as the client is sending something
        chunks = []
        while True:
            chunk = connection.recv(1024)
            print(chunk)
            if not chunk:
                break
        
        print("sending back to client...")
        connection.send(str.encode("<h1>hello</h1>"))
        print("sent...")

 
    finally:
        connection.close()