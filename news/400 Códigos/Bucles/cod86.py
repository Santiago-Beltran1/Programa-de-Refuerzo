SantiagoM = []
for SantiagoF in range(3):
    SantiagoB = []
    for SantiagoCol in range(3):
        valor = int(input(f"Ingrese valor [{SantiagoF},{SantiagoCol}]: "))
        SantiagoB.append(valor)
    SantiagoM.append(SantiagoB)

for SantiagoF in range(3):
    SantiagoSuma = sum(SantiagoM[SantiagoF])
    print(f"Suma fila {SantiagoF+1}: {SantiagoSuma}")
