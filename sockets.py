import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))
server_socket.listen()
print('Server started. Listening...')

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection started: {address}')

    while True:
        request = client_socket.recv(1024)

        if request:
            message_in = request.decode()
            print(f'Message from {address}: {message_in}')
            message_out = 'I read you.\n'.encode()
            client_socket.send(message_out)
        else:
            break

    print(f'Connection finished: {address}')
    client_socket.close()
