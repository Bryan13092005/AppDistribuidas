import threading,time

empresa={
    "S001":["ventas",4],"S002":["Inventario",2],"S003":["contabilidad",5],
    "S004":["compras",3],"S005":["logistica",4]
}

def atencion(codigo):
    print("atendiendo",empresa[codigo][0])
    time.sleep(empresa[codigo][1])
    print("Atendido",empresa[codigo][0])

initialTime=time.perf_counter()#reloj interno

for clave,valor in empresa.items():
    atencion(clave)

finalTime=time.perf_counter()-initialTime

print("Tiempo total secuencial:",finalTime.__round__(2))

initialTimeHilo=time.perf_counter()#reloj interno
hilos=[]
for clave,valor in empresa.items():
    hilo=threading.Thread(target=atencion,args=(clave,))
    hilo.start()
    hilos.append(hilo)

for i in hilos:
    i.join()

finalTimeHilo=time.perf_counter()-initialTimeHilo

print("Tiempo total hilos:",finalTimeHilo.__round__(2))