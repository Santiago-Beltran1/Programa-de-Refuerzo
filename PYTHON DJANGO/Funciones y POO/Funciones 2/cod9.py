import time as SantiagoTime

def SantiagoTemp(SantiagoSegs):
    for SantiagoCont in range(SantiagoSegs, 0, -1):
        print(f"Tiempo restante: {SantiagoCont}")
        SantiagoTime.sleep(1)
    print("Tiempo terminado")

SantiagoTemp(5)
