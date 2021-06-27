import socket
import threading
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))
server_socket.listen()
print('Server started. Listening...')


def handle_client(client_socket, address):
    print(f'Connection started: {address}')
    while True:
        request = client_socket.recv(1024)

        if request:
            message_in = request.decode('utf-8').rstrip()
            print(f'Message from {address}: {message_in}')
            message_out = 'I read you.\n'.encode()
            client_socket.send(message_out)
        else:
            client_socket.close()
            print(f'Connection finished: {address}')
            break


while True:
    client_socket, address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, address)).start()
