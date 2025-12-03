#Simular compra con descuentos

santiagoProds = int(input("¿Cuántos productos desea comprar?: "))

for santiagoI in range(santiagoProds):
    santiagoNom = input(f"Producto {santiagoI+1}: ")
    santiagoPrice = float(input("Precio: "))

    if santiagoPrice > 50000:
        santiagoDesc = 0.2
    elif santiagoPrice > 20000:
        santiagoDesc = 0.1
    else:
        santiagoDesc = 0.05

    santiagoPriceFinal = santiagoPrice - (santiagoPrice * santiagoDesc)
    print(f"{santiagoNom} - Precio final con descuento: ${santiagoPriceFinal}")
