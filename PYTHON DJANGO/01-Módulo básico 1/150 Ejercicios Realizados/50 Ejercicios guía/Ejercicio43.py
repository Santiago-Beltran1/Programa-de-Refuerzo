#Invertir un número entero sin convertir a cadena

def santiagoInverNum(santiagoN):
    santiagoInver = 0
    while santiagoN > 0:
        santiagoInver = santiagoInver * 10 + santiagoN % 10
        santiagoN //= 10
    return santiagoInver

print(santiagoInverNum(12345))  
