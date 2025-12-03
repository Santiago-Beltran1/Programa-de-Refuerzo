#Agregar y ordenar los productos

santiagoComps = []

while True:
    santiagoProd = input("Producto a agregar (o 'fin'): ")
    if santiagoProd == "fin":
        break
    santiagoComps.append(santiagoProd)

santiagoComps.sort()
print("Lista de compras ordenada:", santiagoComps)
