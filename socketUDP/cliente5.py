import socket,json,time
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

direccionServidor=('127.0.0.1',5000)

def enviarServidor(datosEnviarServidor,valor):
    datosParaEnvio={valor:datosEnviarServidor}
    datosJson=json.dumps(datosParaEnvio)
    servidor_socket.sendto(datosJson.encode(),direccionServidor)
    data,direccion=servidor_socket.recvfrom(1024)

    mensaje=data.decode()
    print("---------------RESULTADO RECIBIDO------------------")
    mensajeDecodificado=json.loads(mensaje)
    print('Direccion cliente:',direccion)
    tipoPeticion = int(list(mensajeDecodificado.keys())[0])
    if(tipoPeticion==1):
        if(mensajeDecodificado['1']=='Usuario ya existente'):
            print('El usuario ya existe')
            return

        print(mensajeDecodificado['1'])

    if(tipoPeticion==2):
        if(mensajeDecodificado['2']=='no encontrado'):
            print('Usuario no encontrado en el servidor')
            return
        
        usuario=mensajeDecodificado['2']
        print(f'''------------------- DATOS USUARIO ------------------
        CEDULA: {usuario['cedula']}
        NOMBRE: {usuario['nombre']}
        CORREO: {usuario['correo']}
        SALDO ACTUAL: ${usuario['saldo']}''')

    if(tipoPeticion==3):
        if(mensajeDecodificado['3']=='no encontrado'):
            print('Usuario no encontrado en el servidor')
            return
        
        usuario=mensajeDecodificado['3']
        print(f'''------------------- OPERACION EXISTOSA ------------------
        CEDULA: {usuario['cedula']}
        SALDO ACTUAL: ${usuario['saldo']}''')

def crearUsuario(nombre,cedula,correo,saldo):
    datosEnviar={
        'cedula':cedula,
        'nombre':nombre,
        'correo':correo,
        'saldo':saldo
    }
    enviarServidor(datosEnviar,1)

def consultarUsuario(cedula):
    datosEnviar={'cedula':cedula}
    enviarServidor(datosEnviar,2)

def recargarSaldo(monto,cedula):
    datosEnviar={'cedula':cedula,
           'monto':monto}
    enviarServidor(datosEnviar,3)

#forma con JSON
while True:
    print(f'''Seleccione una opcion:
    1. Registrar Usuario
    2. Consultar Usuario por cedula
    3. Recargar Usuario
    0. SALIR''')
    opcion=int(input('Ingrese una opcion: '))

    match opcion:
        case 1:
            nombre=input('Ingresa el nombre: ')
            cedula=input('Ingrese la cedula: ')
            correo=input('Ingrese el correo: ')
            saldo=float(input('Ingrese el saldo Inicial: $'))

            if len(nombre) == 0 or len(cedula) != 10 or correo.find('@') == -1 or correo.find('.')==-1 or saldo<0 or not cedula.isdigit():
                print('Valor inválido')
                continue
            print('Enviando Peticion')
            crearUsuario(nombre,cedula,correo,saldo)

        case 2:
            cedula=input('Ingrese la cedula del usuario: ')
            if len(cedula)!=10 or not cedula.isdigit():
                print('Valor inválido')
                continue
            print('Enviando Peticion')
            consultarUsuario(cedula)

        case 3:
            cedula=input('Ingrese la cedula del usuario: ')
            saldo=float(input('Ingrese el saldo a enviar: $'))
            if len(cedula)!=10 or not cedula.isdigit() or saldo<=0:
                print('Valor inválido')
                continue
            print('Enviando Peticion')
            recargarSaldo(saldo,cedula)
        case 0:
            print('Saliendo...')
            break
        case _:
            print('Opcion inválida')
            continue



#servidor_socket.close()