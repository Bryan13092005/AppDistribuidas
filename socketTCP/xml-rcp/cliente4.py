import xmlrpc.client


cliente = xmlrpc.client.ServerProxy("http://172.31.116.80:8000")

def menu():
    print("Seleccione una conversión:")
    print("1. C° a F°")
    print("2. F° a C°")
    print("3. C° a K°")
    print("4. K° a C°")
    print("5. K° a F°")
    print("6. F° a K°")
    print("7. Salir")

while True:
    menu()
    opcion=input("Ingrese el numero de la conversión que desea realizar: ")
    if opcion=="1":
        celcius=float(input("Ingrese la temperatura en Celsius: "))
        resultado=cliente.celFar(celcius)
        print("Resultado:", resultado, "F°")
    elif opcion=="2":
        fahrenheit=float(input("Ingrese la temperatura en Fahrenheit: "))
        resultado=cliente.farCel(fahrenheit)
        print("Resultado:", resultado, "C°")
    
    elif opcion=="3":
        celcius=float(input("Ingrese la temperatura en Celsius: "))
        resultado=cliente.celKel(celcius)
        print("Resultado:", resultado, "K°")
    elif opcion=="4":
        kelvin=float(input("Ingrese la temperatura en Kelvin: "))
        resultado=cliente.kelCel(kelvin)
        print("Resultado:", resultado, "C°")
    elif opcion=="5":
        kelvin=float(input("Ingrese la temperatura en Kelvin: "))
        resultado=cliente.kelFar(kelvin)
        print("Resultado:", resultado,"F°")
    elif opcion=="6":
        fahrenheit=float(input("Ingrese la temperatura en Fahrenheit: "))
        resultado=cliente.farKel(fahrenheit)
        print("Resultado:", resultado, "K°")
    elif opcion=="7":
        break
    else:
        print("Opción no válida")