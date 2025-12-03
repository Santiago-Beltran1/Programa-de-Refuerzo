#Sumar todos los números pares dentro de un rango dado

def santiagoSumPares(inicio, fin):
    santiagoSum = 0
    for santiagoNum in range(inicio, fin + 1):
        if santiagoNum % 2 == 0:
            santiagoSum += santiagoNum
    return santiagoSum

print(santiagoSumPares(1, 10)) 
