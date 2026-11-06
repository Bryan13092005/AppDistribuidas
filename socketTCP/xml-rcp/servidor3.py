from xmlrpc.server import SimpleXMLRPCServer

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def dividir(a,b):
    if b==0:
        return 'no valido'
    return a/b

def producto(a,b):
    return a*b

servidor=SimpleXMLRPCServer(('0.0.0.0',8000))
servidor.register_function(sumar,'suma')
servidor.register_function(restar,'resta')
servidor.register_function(dividir,'division')
servidor.register_function(producto,'multiplicacion')

servidor.serve_forever()