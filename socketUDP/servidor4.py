import socket, threading,json
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor_socket.bind(("0.0.0.0",5000))
print('esperando conexiones')

def tarea(data,direccion):
    mensaje=data.decode()
    print("---------------------------------")
    mensajeDecodificado=json.loads(mensaje)
    print('Direccion cliente:',direccion)
    print('Codigo:',mensajeDecodificado['codigo'])
    print('Sensor:',mensajeDecodificado['sensor'])
    print('Medida:',mensajeDecodificado['valor'])
    respuesta="DATOS RECIBIDOS CORRECTAMENTE"
    servidor_socket.sendto(respuesta.encode(),direccion)

while True:
    data,addr=servidor_socket.recvfrom(1024)
    hilo=threading.Thread(target=tarea,args=(data,addr))
    hilo.start()


#servidor_socket.close()