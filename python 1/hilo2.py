import threading

def tareaHiloA():
    for i in range(5):
        print('HILO A: A',i);

def tareaHiloB():
    for i in range(5):
        print('HILO B: B',i);

for i in range(5):
    print('HILO PRINCIPAL: P',i);

hiloA=threading.Thread(target=tareaHiloA);
hiloA.start();
hiloB=threading.Thread(target=tareaHiloB);
hiloB.start();