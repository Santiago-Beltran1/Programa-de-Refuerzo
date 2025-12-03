SantiagoB = []
for SantiagoI in range(4):
    SantiagoNum = int(input("Ingrese un número: "))
    SantiagoB.append(SantiagoNum)

SantiagoBus = int(input("Ingrese un número a buscar: "))
SantiagoEncon = False

for SantiagoN in SantiagoB:
    if SantiagoN == SantiagoBus:
        SantiagoEncon = True
        break

if SantiagoEncon:
    print("Número encontrado.")
else:
    print("Número no encontrado.")
