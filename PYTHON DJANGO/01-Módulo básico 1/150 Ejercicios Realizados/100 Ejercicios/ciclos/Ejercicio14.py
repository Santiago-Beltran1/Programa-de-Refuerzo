#Determinar tipo de triángulo

santiagoA = float(input("Lado 1: "))
santiagoB = float(input("Lado 2: "))
santiagoC = float(input("Lado 3: "))

if santiagoA == santiagoB == santiagoC:
    print("Equilátero")
elif santiagoA == santiagoB or santiagoB == santiagoC or santiagoA == santiagoC:
    print("Isósceles")
else:
    print("Escaleno")
