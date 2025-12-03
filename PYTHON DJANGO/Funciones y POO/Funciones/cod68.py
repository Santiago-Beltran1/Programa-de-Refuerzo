import time

def SantiagoBTemporizador(SantiagoSegundos, SantiagoMensaje):
    print(f"Esperando {SantiagoSegundos} segundos...")
    time.sleep(SantiagoSegundos)
    print(SantiagoMensaje)

SantiagoSeg = int(input("Segundos: "))
SantiagoMsg = input("Mensaje al finalizar: ")
SantiagoBTemporizador(SantiagoSeg, SantiagoMsg)
