#Menú básico de operaciones

print("1. Suma  2. Resta  3. Multiplicación  4. División")
santiagoOp = int(input("Seleccione una opción: "))
santiagoA = float(input("Número 1: "))
santiagoB = float(input("Número 2: "))

if santiagoOp == 1:
    print("Resultado:", santiagoA + santiagoB)
elif santiagoOp == 2:
    print("Resultado:", santiagoA - santiagoB)
elif santiagoOp == 3:
    print("Resultado:", santiagoA * santiagoB)
elif santiagoOp == 4:
    if santiagoB != 0:
        print("Resultado:", santiagoA / santiagoB)
    else:
        print("Error: división por cero")
else:
    print("Opción no válida")
