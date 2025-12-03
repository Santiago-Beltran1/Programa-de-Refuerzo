#Contador de pares e impares según hasta el rango limite dado

santiagoPares = 0
santiagoImpares = 0
santiagoLimit = int(input("Ingrese hasta qué número contar: "))

for santiagoI in range(1, santiagoLimit+1):
    if santiagoI % 2 == 0:
        santiagoPares += 1
    else:
        santiagoImpares += 1

print(f"Cantidad de números pares: {santiagoPares}")
print(f"Cantidad de números impares: {santiagoImpares}")
