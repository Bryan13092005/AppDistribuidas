import socket
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
direccionServidor=('172.31.116.79',5000)
mensaje2=input('Ingrese el mensaje para el servidor')

servidor_socket.sendto(mensaje2.encode(),direccionServidor)
data,addr=servidor_socket.recvfrom(1024)

print("Mensaje recibido:",data.decode(),"de:",addr)


#servidor_socket.close()