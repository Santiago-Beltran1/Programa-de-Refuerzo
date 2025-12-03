import random

SantiagoObjt = random.randint(1, 15)
SantiagoB = -1
SantiagoIn = 0

while SantiagoB != SantiagoObjt:
    SantiagoB = int(input("Adivine el número entre 1 y 20: "))
    SantiagoIn += 1
    if SantiagoB < SantiagoObjt:
        print("Muy bajo")
    elif SantiagoB > SantiagoObjt:
        print("Muy alto")
    else:
        print(f"Lo a adivinado en {SantiagoIn} intentos")
