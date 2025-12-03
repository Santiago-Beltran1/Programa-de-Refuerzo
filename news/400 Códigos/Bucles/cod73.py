SantiagoB = []
while True:
    SantiagoProd = input("Ingrese producto (o 'fin' para terminar): ")
    if SantiagoProd.lower() == "fin":
        break
    SantiagoCosto = float(input("Precio: "))
    SantiagoB.append(SantiagoCosto)

SantiagoTotal = sum(SantiagoB)
print(f"El total a pagar en toda la compra es: {SantiagoTotal}")
