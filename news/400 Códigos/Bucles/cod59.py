SantiagoB = [11, 5, 1, 5, 65, 51, 22, 11]
SantiagoMin = SantiagoB[0]
SantiagoMax = SantiagoB[0]
for SantiagoB in SantiagoB:
    if SantiagoB < SantiagoMin:
        SantiagoMin = SantiagoB
    if SantiagoB > SantiagoMax:
        SantiagoMax = SantiagoB
print(f"Número mínimo: {SantiagoMin} - Número Máximo: {SantiagoMax}")
