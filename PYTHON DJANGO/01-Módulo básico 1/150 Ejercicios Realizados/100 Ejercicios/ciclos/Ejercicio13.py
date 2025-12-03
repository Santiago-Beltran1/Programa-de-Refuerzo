#Comparar dos números

santiagoA = float(input("Ingrese el primer número: "))
santiagoB = float(input("Ingrese el segundo número: "))

if santiagoA > santiagoB:
    print(f"{santiagoA} es mayor que {santiagoB}")
elif santiagoA < santiagoB:
    print(f"{santiagoB} es mayor que {santiagoA}")
else:
    print("Son iguales")
