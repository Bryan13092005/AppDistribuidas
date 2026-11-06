import socket, threading
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor_socket.bind(("0.0.0.0",5000))
print('esperando conexiones')

def tarea(data,direccion):
    
    print("Mensaje recibido:",data.decode(),"de:",direccion)

    respuesta="HOLA soy el servidor"
    servidor_socket.sendto(respuesta.encode(),direccion)

while True:
    data,addr=servidor_socket.recvfrom(1024)
    hilo=threading.Thread(target=tarea,args=(data,addr))
    hilo.start()


#servidor_socket.close()