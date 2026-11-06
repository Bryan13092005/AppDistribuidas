import socket
import threading

socketServer=socket. socket(socket.AF_INET, socket. SOCK_STREAM)
socketServer.bind(("0.0.0.0",5000))
socketServer. listen()
print("Esperando conexiones..... ")

def tarea(conn,addr):
    print('cliente conectado:', addr)
    mensaje = conn.recv(1024)

    print('mensaje:', mensaje.decode())

    respuesta = 'hola soy el servidor 2'
    conn.send(respuesta.encode())

    conn.close()
    print('cliente desconectado')

while True:
    conexion, direccion=socketServer.accept()
    hilo=threading.Thread(target=tarea, args=(conexion,direccion))
    hilo.start()