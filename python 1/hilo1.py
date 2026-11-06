import threading

def tarea():
    print('Soy hilo secundario');

print('Soy hilo principal');

hilo=threading.Thread(target=tarea);
hilo.start();