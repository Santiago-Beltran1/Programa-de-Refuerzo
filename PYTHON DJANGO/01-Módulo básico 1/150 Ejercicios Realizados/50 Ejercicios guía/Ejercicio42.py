#Calculadora de promedio pero con números que se ponen con coma

santiagoNums = input("Ingresa números separados por coma: ").split(",")
santiagoNums = [float(n) for n in santiagoNums]
santiagoProm = sum(santiagoNums) / len(santiagoNums)

print("La suma de todos los numeros es:", sum(santiagoNums))
print("El promedio es:", santiagoProm)
