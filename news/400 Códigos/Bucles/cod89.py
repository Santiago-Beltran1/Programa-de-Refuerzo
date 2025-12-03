SantiagoTot = 0

while True:
    SantiagoB = input("Producto vendido o 'fin': ").lower()
    if SantiagoB == "fin":
        break
    SantiagoPrecio = float(input("Precio del producto: "))
    SantiagoTot += SantiagoPrecio
    print("Total acumulado:", SantiagoTot)

print(f"Se cierra la caja. Total vendido: {SantiagoTot}")
