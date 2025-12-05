import time

def SantiagoTemporizador(SantiagoSeg):
    for SantiagoI in range(SantiagoSeg, 0, -1):
        print(f"Tiempo restante: {SantiagoI} segundos")
        time.sleep(1)
    print("¡Tiempo terminado!")

SantiagoSeg = int(input("Ingresa segundos del temporizador: "))
SantiagoTemporizador(SantiagoSeg)
