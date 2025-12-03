#EJERCICIOS FINALES - Simulador de tienda online

santiagoInv = {"manzanas": 10, "naranjas": 5}
santiagoCar = {}

def santiagoMosInv():
    print("Inventario:")
    for santiagoPro, santiagoCant in santiagoInv.items():
        print(f"{santiagoPro}: {santiagoCant}")

def santiagoAgCar(santiagoProd, santiagoCant):
    if santiagoProd in santiagoInv and santiagoInv[santiagoProd] >= santiagoCant:
        santiagoCar[santiagoProd] = santiagoCar.get(santiagoProd, 0) + santiagoCant
        santiagoInv[santiagoProd] -= santiagoCant
        print(f"{santiagoCant} {santiagoProd} agregadas al carrito.")
    else:
        print("No hay suficiente stock.")

def santiagoPedido():
    if santiagoCar:
        print("Pedido procesado:")
        for santiagoProd, santiagoCant in santiagoCar.items():
            print(f"{santiagoCant} x {santiagoProd}")
        santiagoCar.clear()
    else:
        print("Carrito vacío.")

santiagoMosInv()
santiagoAgCar("manzanas", 3)
santiagoPedido()
santiagoMosInv()
