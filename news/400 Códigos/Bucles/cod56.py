SantiagoB_Matriz = [
    [48, 12, 74],
    [75, 11, 41],
    [42, 32, 5]
]
SantiagoSum = 0
for SantiagoBF in SantiagoB_Matriz:
    for SantiagoValor in SantiagoBF:
        SantiagoSum += SantiagoValor
print("Suma total de la matriz es igual a:", SantiagoSum)
