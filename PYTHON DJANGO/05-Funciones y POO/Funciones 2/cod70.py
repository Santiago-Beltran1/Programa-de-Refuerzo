def SantiagoCalcPag(SantiagoHoras, SantiagoTarifa, SantiagoHorasExtra=0, SantiagoTarifaExtra=0):
    SantiagoPago = SantiagoHoras * SantiagoTarifa
    SantiagoPagoExtra = SantiagoHorasExtra * SantiagoTarifaExtra
    return SantiagoPago + SantiagoPagoExtra

print(SantiagoCalcPag(40, 10, 5, 15))
