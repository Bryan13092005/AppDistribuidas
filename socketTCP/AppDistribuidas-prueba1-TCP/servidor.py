import threading, json, socket
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind(("0.0.0.0",5000))
servidor_socket.listen()
print('esperando conexiones')

turnos=[]

def enviarRespuesta(mensaje,codigo,conn):
    enviarDatos={codigo:mensaje}
    enviarDatos=json.dumps(enviarDatos)
    conn.send(enviarDatos.encode())

def caso1(data):
    if(data['nombre']=='' or data['nombre'].__len__()==0):
        print({'mensaje':f'''El nombre es obligatorio para asignar turnos'''})
    contador=0
    for turno in turnos:
        contador+=1
    turnoAsignado=contador+1
    turnos.append({'nombre':data['nombre'],
                   'turno':turnoAsignado,
                   'estado':0})

    print({'mensaje':f'''Su turno es: {turnoAsignado}'''})
    return {'mensaje':f'''Su turno es: {turnoAsignado}'''}

def caso2():
    indice=(turnos.__len__())-1

    if(indice==-1):
        return {'mensaje':'No hay Usuarios Registrados'}
    
    ultimoTurno=turnos[indice]
    print(turnos)
    return {'mensaje':f'''El último turno asignado fue {ultimoTurno['turno']}, para {ultimoTurno['nombre']}'''}

def caso3():
    encontrado=False
    indice=0

    for turno in turnos:
        if turno['estado']==0:
            encontrado=True
            print(turnos.index(turno))
            indice=turnos.index(turno)
            break
        

    if(encontrado):
        usuario=turnos[indice]
        usuario['estado']=1
        return {'mensaje':f'''El turno Atendido fue #{usuario['turno']}, del paciente {usuario['nombre']}'''}

    return {'mensaje':'No hay pacientes para atender'}


def caso4():
    contador=0

    for turno in turnos:
        if turno['estado']==0:
            contador+=1

    return {'mensaje':f'''El número de turnos por atender es: {contador}'''}

def tarea(data,conn):
    mensaje=data
    print("---------------PETICION RECIBIDA------------------")
    mensajeDecodificado=json.loads(mensaje)
    print(mensajeDecodificado)
    print('Direccion cliente:',conn)
    tipoPeticion = int(list(mensajeDecodificado.keys())[0])
    if(tipoPeticion==1):
        mensaje=caso1(mensajeDecodificado['1'])
        enviarRespuesta(mensaje,1,conn)

    if(tipoPeticion==2):
        mensaje=caso2()
        enviarRespuesta(mensaje,2,conn)

    if(tipoPeticion==3):
        mensaje=caso3()
        enviarRespuesta(mensaje,3,conn)

    if(tipoPeticion==4):
        mensaje=caso4()
        enviarRespuesta(mensaje,4,conn)




while True:
    conn,addr=servidor_socket.accept()
    print('cliente conectado:', addr)
    while True:
        data=conn.recv(1024)    
        if not data:
            break
        datos=data.decode()
        hilo=threading.Thread(target=tarea,args=(datos,conn))
        hilo.start()

    conn.close()
    print('cliente desconectado')