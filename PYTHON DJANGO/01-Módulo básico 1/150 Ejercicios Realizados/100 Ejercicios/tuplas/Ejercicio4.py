#Simulador de compra en un restaurante según el menú

santiagoMen = (("Hamburguesa", 12000), ("Perro caliente", 8000), ("Pizza", 15000))
santiagoTotal = 0

for santiagoPlato, santiagoPrec in santiagoMen:
    print(f"{santiagoPlato} - ${santiagoPrec}")
    santiagoComp = input(f"¿Comprar {santiagoPlato}? (si/no): ")
    if santiagoComp == "si":
        santiagoTotal += santiagoPrec

print("Total a pagar:", santiagoTotal)
