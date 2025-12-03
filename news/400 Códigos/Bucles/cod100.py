import numpy as np

SantiagoB = int(input("Filas y columnas de la matriz cuadrada: "))
SantiagoMat = np.zeros((SantiagoB,SantiagoB))

for SantiagoI in range(SantiagoB):
    for SantiagoJ in range(SantiagoB):
        SantiagoMat[SantiagoI,SantiagoJ] = float(input(f"Elemento [{SantiagoI+1},{SantiagoJ+1}]: "))

print("Matriz ingresada:")
print(SantiagoMat)
print(f"Suma de la matriz en la primera diagonal: {np.trace(SantiagoMat)}")
