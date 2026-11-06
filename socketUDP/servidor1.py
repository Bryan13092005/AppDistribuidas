import socket
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor_socket.bind(("localhost",5000))
while True:
    data,addr=servidor_socket.recvfrom(1024)

    print("Mensaje recibido:",data.decode(),"de:",addr)

    respuesta="HOLA soy el servidor"
    servidor_socket.sendto(respuesta.encode(),addr)


#servidor_socket.close()