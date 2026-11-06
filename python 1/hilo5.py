import threading

contador=0

def aumentar(hilo):
    global contador
    for i in range (3):
        aux=contador
        print(hilo,"lee",aux)
        aux=aux+i
        contador=aux
        print(hilo,"escribe",contador)


hiloA=threading.Thread(target=aumentar,args=("A"))
hiloB=threading.Thread(target=aumentar,args=("B"))
hiloA.start()
hiloB.start()
