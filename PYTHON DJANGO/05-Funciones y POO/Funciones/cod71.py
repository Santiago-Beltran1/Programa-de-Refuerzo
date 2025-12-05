import random

def SantiagoBMoneda():
    SantiagoBResultado = random.choice(["Cara", "Cruz"])
    return SantiagoBResultado

print("Lanzando moneda")
print("Resultado:", SantiagoBMoneda())
