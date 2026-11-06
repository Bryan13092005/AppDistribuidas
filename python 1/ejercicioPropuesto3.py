import threading

contador = 0
bloqueo = threading.Lock()
turnos = {}

def asignarTurno(cliente):
    global contador
    with bloqueo:
        contador += 1
        turno = contador
        print("Turno", turno, "asignado.")
    turnos[cliente] = turno

hilos = []
for i in range(3):
    cliente = "Cliente " + str(i + 1)
    hilo = threading.Thread(target=asignarTurno, args=(cliente,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

for cliente, turno in turnos.items():
    print(cliente, "recibió el turno", turno)