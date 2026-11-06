import socket

socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketCliente.connect(('localhost',5000))


mensaje = 'Hola soy el cliente'
socketCliente.send(mensaje.encode())

respuesta = socketCliente.recv(1024)

print('respuesta:', respuesta.decode())

socketCliente.close()