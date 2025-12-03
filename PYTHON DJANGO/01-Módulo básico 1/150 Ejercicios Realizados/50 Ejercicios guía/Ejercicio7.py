# Calculadora de descuento 
santiagoTotal = 10000
santiagoDesc = 0 
if santiagoTotal > 5000: 
    santiagoDesc = santiagoTotal * 0.20 
    santiagoFinal = santiagoTotal - santiagoDesc
    print("Obtiene un descuento del 20%")
    print("Descuento aplicado: $", santiagoDesc)
else:
    santiagoFinal = santiagoTotal
    print("No hay descuento disponible")
print("Precio original: $", santiagoTotal)
print("Precio final: $", santiagoFinal)