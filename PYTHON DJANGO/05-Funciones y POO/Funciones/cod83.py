import random

def SantiagoBAdivinar():
    SantiagoBNumero = random.randint(1, 50)
    SantiagoInten = 0
    while True:
        SantiagoBIntento = int(input("Adivina el número (1-50): "))
        SantiagoInten += 1
        if SantiagoBIntento < SantiagoBNumero:
            print("Muy bajo")
        elif SantiagoBIntento > SantiagoBNumero:
            print("Muy alto")
        else:
            print(f"Acerto en {SantiagoInten} intentos")
            break

SantiagoBAdivinar()
