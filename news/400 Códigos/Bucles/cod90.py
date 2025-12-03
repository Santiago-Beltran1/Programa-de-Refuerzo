SantiagoLimit = 100000
SantiagoPres = 0

while SantiagoPres < SantiagoLimit:
    SantiagoB = float(input("Monto a prestar: "))
    if SantiagoPres + SantiagoB <= SantiagoLimit:
        SantiagoPres += SantiagoB
        print("Préstamo aprobado. Total prestado:", SantiagoPres)
    else:
        print("Excede el límite")

print("Límite alcanzado")
