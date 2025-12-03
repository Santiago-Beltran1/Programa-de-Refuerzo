#Ingreso de productos

santiagoInv = {"sillas": 10, "camisetas": 8}
print("Inventario inicial:", santiagoInv)

santiagoProd = input("Producto a agregar o actualizar: ")
santiagoCant = int(input("Cantidad: "))
santiagoInv[santiagoProd] = santiagoInv.get(santiagoProd, 0) + santiagoCant

print("Inventario final:", santiagoInv)
