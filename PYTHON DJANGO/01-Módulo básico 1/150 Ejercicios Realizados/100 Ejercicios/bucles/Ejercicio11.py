#Imprimir la suma de unos números hasta el rango ingresado en este caso 5

santiagoSum = 0
for santiagoI in range(5):
    santiagoNum = float(input(f"Ingrese número {santiagoI+1}: "))
    santiagoSum += santiagoNum
print("La suma total es:", santiagoSum)
