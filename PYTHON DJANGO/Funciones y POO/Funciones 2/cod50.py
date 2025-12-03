import time as SantiagoTime

def SantiagoTemp(SantiagoSegs, SantiagoMnsj):
    for SantiagoCont in range(SantiagoSegs, 0, -1):
        print(f"Tiempo restante: {SantiagoCont}")
        SantiagoTime.sleep(1)
    print(f"Mensaje: {SantiagoMnsj}")

SantiagoTemp(5, "Se acabo el tiempo")
