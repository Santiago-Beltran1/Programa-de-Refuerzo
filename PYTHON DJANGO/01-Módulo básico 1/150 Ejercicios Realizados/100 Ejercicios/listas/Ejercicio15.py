#Mercadeo básico

santiagoProds = ["Galletas", "Gaseosa", "Jabón"]
santiagoCar = []

while True:
    print("\nProductos:", santiagoProds)
    print("Carrito:", santiagoCar)
    print("1. Agregar al carrito")
    print("2. Quitar del carrito")
    print("3. Salir")
    santiagoOp = input("Opción: ")

    if santiagoOp == "1":
        santiagoP = input("Producto: ")
        if santiagoP in santiagoProds:
            santiagoCar.append(santiagoP)
        else:
            print("No está en la tienda")
    elif santiagoOp == "2":
        santiagoP = input("Producto a quitar: ")
        if santiagoP in santiagoCar:
            santiagoCar.remove(santiagoP)
        else:
            print("No está en el carrito")
    elif santiagoOp == "3":
        break
