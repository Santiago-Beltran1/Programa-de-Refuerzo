def SantiagoTiempoDescarga(SantiagoTamanoMB, SantiagoVelocidadMBps):
    SantiagoSegundos = SantiagoTamanoMB / SantiagoVelocidadMBps
    return round(SantiagoSegundos / 60, 2)

def SantiagoDescarga():
    SantiagoTamano = float(input("Tamaño del archivo (MB): "))
    SantiagoVelocidad = float(input("Velocidad de descarga (MB/s): "))
    print("Tiempo estimado (minutos):", SantiagoTiempoDescarga(SantiagoTamano, SantiagoVelocidad))

SantiagoDescarga()
