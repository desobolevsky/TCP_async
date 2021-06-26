import socket
from select import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))
server_socket.listen()
print('Server started. Listening...')

sockets_to_wait = [server_socket]  # main server socket + client sockets

while True:
    sockets_to_read, _, _ = select(sockets_to_wait, [], [])
    for socket in sockets_to_read:
        if socket is server_socket:
            client_socket, address = server_socket.accept()
            sockets_to_wait.append(client_socket)
            print(f'Connection started: {address}')
        else:
            request = socket.recv(1024)
            address = socket.getpeername()
            if request:
                message_in = request.decode('utf-8').rstrip()
                print(f'Message from {address}: {message_in}')
                message_out = 'I read you.\n'.encode()
                socket.send(message_out)
            else:
                print(f'Connection finished: {address}')
                socket.close()
                sockets_to_wait.remove(socket)
