import xmlrpc.client
cliente=xmlrpc.client.ServerProxy('http://localhost:8000/')


def menu():
    opcion=int(input(f'''
----------------- CALCULADORA --------------
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
0. Salir

Seleccione una opcion: '''))

    return opcion

def pedirNumeros():
    a=float(input('Ingrese el valor a: '))
    b=float(input('Ingrese el valor b: '))

    return a,b

while True:
    opcion=menu()

    if opcion==0:
        print('saliendo')
        break

    a,b=pedirNumeros()
    match opcion:
        case 1:
            print('El resultado es: ',cliente.suma(a,b))
            continue
        case 2:
            print('El resultado es: ',cliente.resta(5,6))
            continue
        case 3:
            print('El resultado es: ',cliente.multiplicacion(5,6))
            continue
        case 4:
            print('El resultado es: ',cliente.division(30,6))
            continue
        case _:
            print('Opcion Incorrecta')
            continue