import random

SantiagoB = 0
SantiagoA = 0

while SantiagoB < 3:
    SantiagoNum1 = random.randint(1, 10)
    SantiagoNum2 = random.randint(1, 10)
    SantiagoResp = int(input(f"¿Cuánto es {SantiagoNum1} + {SantiagoNum2}? "))
    if SantiagoResp == SantiagoNum1 + SantiagoNum2:
        print("Correcto")
        SantiagoA += 1
    else:
        print("Incorrecto")
    SantiagoB += 1

print("Aciertos totales:", SantiagoA)
