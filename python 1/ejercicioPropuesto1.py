import threading

bloqueo=threading.Lock()

def imprimir(hilo):
    with bloqueo:
        print("Hilo ",hilo," esta imprimiendo su conjunto de números:")
        for i in range (5):
            print("Hilo ",hilo," número ",i)
        print("Hilo ",hilo," ha terminado.")
        
for i in range(11):
    valorHilo=i+1
    hilo=threading.Thread(target=imprimir,args=(valorHilo,))
    hilo.start()
