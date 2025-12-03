SantiagoBInv = []
SantiagoTot = 0
SantiagoCant = int(input("Ingrese la cantidad de productos: "))

for SantiagoI in range(SantiagoCant):
    SantiagoNom = input("Nombre del producto: ")
    SantiagoCosto = float(input("Precio unitario: "))
    SantiagoCantProd = int(input("Cantidad disponible: "))
    SantiagoSubtot = SantiagoCosto * SantiagoCantProd
    SantiagoBInv.append((SantiagoNom, SantiagoCosto, SantiagoCantProd, SantiagoSubtot))
    SantiagoTot += SantiagoSubtot

print("\nInventario actual:")
for SantiagoProd in SantiagoBInv:
    print(f"Producto: {SantiagoProd[0]} | Cantidad: {SantiagoProd[2]} | Subtotal: {SantiagoProd[3]}")

print("\nValor total del inventario:", SantiagoTot)
