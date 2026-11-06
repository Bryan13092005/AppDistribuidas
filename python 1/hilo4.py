import threading

def tareaD(hilo):
    for i in range(5):
        print('Hilo',hilo,":",i)

hiloA=threading.Thread(target=tareaD, args=("A",))
hiloB=threading.Thread(target=tareaD, args=("B",))
hiloA.start()
hiloB.start()
hiloA.join()#primero hilo A
hiloB.join()#luego hilo B

#luego programa principal
for i in range(5):
    print('HILO PRINCIPAL: P',i);
