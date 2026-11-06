import socket

socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketCliente.connect(('localhost',5000))

while True:
    mensaje = input('Ingresa el mensaje para el servidor: ')

    if mensaje == 'salir':
        break

    socketCliente.send(mensaje.encode())

    respuesta = socketCliente.recv(1024)

    print('respuesta:', respuesta.decode())

socketCliente.close()