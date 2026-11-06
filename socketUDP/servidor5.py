import socket, threading,json
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor_socket.bind(("0.0.0.0",5000))
print('esperando conexiones')
usuarios=[]
def agregarUsuario(datos,add):
    informacionFinal=''
    cedula=datos['cedula']
    encontrado=False
    for usuario in usuarios:
        if cedula==usuario['cedula']:
            informacionFinal= 'Usuario ya existente'
            encontrado=True
            break
    if not encontrado:
        usuarios.append(datos)
        informacionFinal= 'Usuario Agregado con exitosamente'
    
    print(usuarios)
    enviarResultado(1,informacionFinal,add)

def consultarUsuario(datos,add):
    cedula=datos['cedula']
    encontrado=False
    informacionFinal=''
    for usuario in usuarios:
        if cedula==usuario['cedula']:
            informacion=usuario
            encontrado=True
            informacionFinal= informacion
            break
    if not encontrado:
        informacionFinal= 'No encontrado'

    enviarResultado(2,informacionFinal,add)
    
def recargarSaldo(datos,add):
    cedula=datos['cedula']
    monto=float(datos['monto'])
    print(cedula)
    print(monto)
    encontrado=False
    informacionFinal=''
    for usuario in usuarios:
        if cedula==usuario['cedula']:
            encontrado=True
            usuario['saldo'] = float(usuario['saldo']) + monto
            informacionFinal={'cedula':cedula,'saldo':usuario['saldo']}
            break
    if not encontrado:
        informacionFinal= 'No encontrado'

    enviarResultado(3,informacionFinal,add)

def enviarResultado(tipo,informacionEnviar,direccionCliente):
    respuesta=json.dumps({tipo:informacionEnviar})
    servidor_socket.sendto(respuesta.encode(),direccionCliente)


def tarea(data,direccion):
    mensaje=data.decode()
    print("---------------PETICION RECIBIDA------------------")
    mensajeDecodificado=json.loads(mensaje)
    print(mensajeDecodificado)
    print('Direccion cliente:',direccion)
    tipoPeticion = int(list(mensajeDecodificado.keys())[0])
    if(tipoPeticion==1):
        agregarUsuario(mensajeDecodificado['1'],direccion)

    if(tipoPeticion==2):
        consultarUsuario(mensajeDecodificado['2'],direccion)

    if(tipoPeticion==3):
        recargarSaldo(mensajeDecodificado['3'],direccion)

while True:
    data,addr=servidor_socket.recvfrom(1024)
    hilo=threading.Thread(target=tarea,args=(data,addr))
    hilo.start()


#servidor_socket.close()