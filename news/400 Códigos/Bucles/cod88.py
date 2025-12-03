SantiagoProd = {"laptop": [5000000, 6000000], "Iphone": [5000000, 7000000], "Equipo de Sonido": [100000, 100000]}
# [costo, precio_venta]
for SantiagoB, SantiagoVals in SantiagoProd.items():
    SantiagoCosto, SantiagoVent = SantiagoVals
    if SantiagoVent > SantiagoCosto:
        print(f"{SantiagoB}: Ganancia {SantiagoVent - SantiagoCosto}")
    elif SantiagoVent < SantiagoCosto:
        print(f"{SantiagoB}: Pérdida {SantiagoCosto - SantiagoVent}")
    else:
        print(f"{SantiagoB}: Sin ganancia ni pérdida")
