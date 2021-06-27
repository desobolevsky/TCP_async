import socket
from select import select

tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()
    print('Server started. Listening...')

    while True:
        yield 'read', server_socket
        client_socket, address = server_socket.accept()
        print(f'Connection started: {address}')
        tasks.append(client(client_socket, address))


def client(client_socket, address):
    while True:
        yield 'read', client_socket
        request = client_socket.recv(1024)

        if request:
            message_in = request.decode('utf-8').rstrip()
            print(f'Message from {address}: {message_in}')
            yield 'write', client_socket
            message_out = 'I read you.\n'.encode()
            client_socket.send(message_out)
        else:
            break

    client_socket.close()


tasks.append(server())

while True:
    while tasks:
        try:
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            # Connection closed and the socket was already removed from tasks list
            pass

    ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

    for sock in ready_to_read:
        tasks.append(to_read.pop(sock))

    for sock in ready_to_write:
        tasks.append(to_write.pop(sock))
