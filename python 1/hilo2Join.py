import threading

def tareaHiloA():
    for i in range(5):
        print('HILO A: A',i);

def tareaHiloB():
    for i in range(5):
        print('HILO B: B',i);

hiloA=threading.Thread(target=tareaHiloA);
hiloA.start();
hiloA.join() #hace que termine una tarea antes de empezar la del hilo principal
hiloB=threading.Thread(target=tareaHiloB);
hiloB.start();
hiloB.join()

for i in range(5):
    print('HILO PRINCIPAL: P',i);