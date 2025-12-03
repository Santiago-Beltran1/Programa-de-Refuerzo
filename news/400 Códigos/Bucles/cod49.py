SantiagoB = [101, 255, 200, 125, 5]
SantiagoProm = sum(SantiagoB) / len(SantiagoB)
SantiagoMax = 0
for SantiagoB in SantiagoB:
    if SantiagoB > SantiagoProm:
        SantiagoMax += 1
print(f"El promedio de todos los números de la lista es: {SantiagoProm}")
print(f"Todos los números mayores al promedio que dan entre ellos son: {SantiagoMax}")
