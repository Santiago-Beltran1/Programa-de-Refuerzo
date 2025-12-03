SantiagoB = []
SantiagoCant = int(input("Ingrese la cantidad de notas: "))

for SantiagoI in range(SantiagoCant):
    SantiagoNota = float(input("Ingrese la nota: "))
    if SantiagoNota >= 3:
        print("Aprobado")
    else:
        print("Reprobado")
    SantiagoB.append(SantiagoNota)

SantiagoProm = sum(SantiagoB) / len(SantiagoB)
print("Promedio general:", SantiagoProm)
