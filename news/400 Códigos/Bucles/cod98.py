import random

SantiagoB = ""
SantiagoCara = 0
SantiagoCruz = 0

while SantiagoB != "fin":
    SantiagoB = input("Lanzar moneda (o 'fin'): ").lower()
    if SantiagoB != "fin":
        SantiagoR = random.choice(["cara","cruz"])
        print("Resultado:", SantiagoR)
        if SantiagoR=="cara":
            SantiagoCara += 1
        else:
            SantiagoCruz += 1

print(f"Total de veces que sale cara: {SantiagoCara} - Total de veces que sale cruz: {SantiagoCruz}")
