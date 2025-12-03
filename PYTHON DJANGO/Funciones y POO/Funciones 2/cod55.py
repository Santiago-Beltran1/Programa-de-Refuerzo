def SantiagoCalDesc(SantiagoCosto, SantiagoPctj):
    SantiagoDesc = SantiagoCosto * SantiagoPctj / 100
    return SantiagoCosto - SantiagoDesc

print(f"El descuento del 30% en una compra de $350.000 es de: {SantiagoCalDesc(350000, 30)}")
