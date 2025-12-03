#Lista con números y mostrar sólo los que son múltiplos de 3
santiagoList = [5, 9, 12, 20, 33, 42, 50]
SantiagoMul3 = []

for santiagoN in santiagoList:
    if santiagoN % 3 == 0:
        SantiagoMul3.append(santiagoN)

print("Números múltiplos de 3:", SantiagoMul3)
