SantiagoB = [
    [4, 111, 10],
    [3, 22, 77],
    [41, 78, 51]
]
print("Números impares de toda la matriz:")
for SantiagoF in SantiagoB:
    for SantiagoValor in SantiagoF:
        if SantiagoValor % 2 != 0:
            print(SantiagoValor, end=" ")
print()
