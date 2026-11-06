import threading
import time

def mensaje(cliente):
    print("Atendiendo",cliente)
    time.sleep(2)
    print(cliente," atendido")

hiloA=threading.Thread(target=mensaje,args=("Cliente 1",))
hiloB=threading.Thread(target=mensaje,args=("Cliente 2",))
hiloC=threading.Thread(target=mensaje,args=("Cliente 3",))

hiloA.start()
hiloB.start()
hiloC.start()
