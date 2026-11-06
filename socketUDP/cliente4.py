import socket,json,time
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sensores={
    'S1':['temperatura',30],
    'S2':['humedad',80],
    'S3':['distancia',20],
    'S4':['Nivel Agua','Medio']
}

direccionServidor=('172.31.116.80',5000)

#forma con JSON
for codigo,datos in sensores.items():
    mensaje2={'codigo':codigo,
              'sensor':datos[0],
              'valor':datos[1]}
    print(mensaje2)

    servidor_socket.sendto(json.dumps(mensaje2).encode(),direccionServidor)
    data,addr=servidor_socket.recvfrom(1024)

    print("Mensaje recibido:",data.decode(),"de:",addr)
    time.sleep(2)


#servidor_socket.close()