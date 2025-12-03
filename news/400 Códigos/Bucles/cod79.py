SantiagoSum = 0
SantiagoCont = 0

while True:
    SantiagoEdad = int(input("Ingrese edad (0 para salir): "))
    if SantiagoEdad == 0:
        break
    SantiagoSum += SantiagoEdad
    SantiagoCont += 1

if SantiagoCont > 0:
    print(f"El promedio de las edades es igual a: {SantiagoSum / SantiagoCont}")
else:
    print("No se ingresaron edades.")
