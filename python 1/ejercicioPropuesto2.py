import threading,time

archivos={
    1:["archivo1.zip",5],
    2:["archivo2.mp4",7],
    3:["archivo3.pdf",3]
}

def descarga(numArchivo):
    print("Descargando",archivos[numArchivo][0],"(",archivos[numArchivo][1],"MB)...")
    #tomando en cuenta 1mb/s
    time.sleep(archivos[numArchivo][1])
    print("Descarga completa:",archivos[numArchivo][0])

for clave,valor in archivos.items():
    hilo=threading.Thread(target=descarga,args=(clave,))
    hilo.start()