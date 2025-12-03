#Alertador de inventario

santiagoProds = int(input("¿Cuántos productos hay en stock?: "))

for santiagoI in range(santiagoProds):
    santiagoNom = input("Nombre del producto: ")
    santiagoCant = int(input("Cantidad en stock: "))

    if santiagoCant == 0:
        print(f"Producto {santiagoNom}: SIN STOCK")
    elif santiagoCant < 5:
        print(f"Producto {santiagoNom}: Stock BAJO")
    else:
        print(f"Producto {santiagoNom}: Stock suficiente")
