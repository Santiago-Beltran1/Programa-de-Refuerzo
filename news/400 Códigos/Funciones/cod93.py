import random

def SantiagoBDiagnostico():
    SantiagoBLatencia = random.randint(10, 150)
    SantiagoBPerdida = random.randint(0, 10)
    print(f"Latencia: {SantiagoBLatencia} ms")
    print(f"Pérdida de paquetes: {SantiagoBPerdida}%")

    if SantiagoBLatencia > 100 or SantiagoBPerdida > 5:
        print("Conexión inestable.")
    else:
        print("Conexión estable.")

SantiagoBDiagnostico()
