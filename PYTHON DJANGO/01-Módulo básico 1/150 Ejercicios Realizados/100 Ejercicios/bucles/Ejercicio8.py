#Calcular suma, promedio y número mayor de todos los que ingrese el usuario

santiagoN = int(input("¿Cuántos números quiere ingresar? "))
santiagoNums = []
for santiagoi in range(santiagoN):
    santiagoNum = float(input(f"Ingrese el número {santiagoi+1}: "))
    santiagoNums.append(santiagoNum)

santiagoSum = sum(santiagoNums)
santiagoProm = santiagoSum / santiagoN
santiagoMayor = max(santiagoNums)

print("La suma total es:", santiagoSum)
print("El promedio es:", santiagoProm)
print("El número mayor es:", santiagoMayor)
