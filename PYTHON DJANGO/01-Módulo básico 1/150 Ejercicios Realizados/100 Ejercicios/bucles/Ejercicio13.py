#Tabla de multiplicar completa  hasta el 12 de un número ingresado

santiagoN = int(input("Ingrese un número: "))
for santiagoI in range(1, 13):
    print(f"{santiagoN} x {santiagoI} = {santiagoN*santiagoI}")
