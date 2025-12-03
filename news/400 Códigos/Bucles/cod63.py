SantiagoBN = int(input("Ingrese el número para generar su tabla: "))
SantiagoLimit = int(input("Ingrese hasta dónde multiplicar: "))

for SantiagoI in range(1, SantiagoLimit + 1):
    print(f"{SantiagoBN} x {SantiagoI} = {SantiagoBN * SantiagoI}")
