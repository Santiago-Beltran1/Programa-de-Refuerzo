SantiagoB = int(input("Ingrese la cantidad de productos: "))
SantiagoDefect = 0

for SantiagoI in range(SantiagoB):
    SantiagoEstad = input(f"Producto {SantiagoI+1} (b = bueno / d = defectuoso): ")
    if SantiagoEstad == "d":
        SantiagoDefect += 1

print("Productos defectuosos:", SantiagoDefect)
print("Porcentaje de fallas:", (SantiagoDefect / SantiagoB) * 100, "%")
