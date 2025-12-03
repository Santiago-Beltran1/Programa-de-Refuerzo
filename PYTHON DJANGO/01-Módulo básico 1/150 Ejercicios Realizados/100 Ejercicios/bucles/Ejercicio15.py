#Ingresar 10 números y el programa imprime cuántos pares e impares hay

santiagoPares = 0
santiagoImpares = 0
for santiagoI in range(10):
    santiagoNum = int(input("Ingrese un número: "))
    if santiagoNum % 2 == 0:
        santiagoPares += 1
    else:
        santiagoImpares += 1
print("Pares:", santiagoPares, "Impares:", santiagoImpares)
