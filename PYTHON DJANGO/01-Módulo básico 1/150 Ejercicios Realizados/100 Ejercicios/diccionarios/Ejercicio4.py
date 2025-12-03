#Calculador de precios según la cantidad guardada

santiagoTienda = {"Manzanas": {"precio": 1000, "cantidad": 5}, "Peras": {"precio": 800, "cantidad": 7}, "Plátanos": {"precio": 500, "cantidad": 10}}

santiagoTotal = 0
for santiagoProd, santiagoDatos in santiagoTienda.items():
    santiagoSubTotal = santiagoDatos["precio"] * santiagoDatos["cantidad"]
    santiagoTotal += santiagoSubTotal
    print(f"{santiagoProd}: Subtotal = {santiagoSubTotal}")

print(f"Total del inventario: {santiagoTotal}")
