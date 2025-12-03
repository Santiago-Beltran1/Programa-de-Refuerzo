#Imprimir el factorial de un número

santiagoN = int(input("Ingrese un número: "))
santiagoFact = 1
for santiagoI in range(1, santiagoN+1):
    santiagoFact *= santiagoI
print("Factorial:", santiagoFact)
