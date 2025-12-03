def SantiagoConvDiv(SantiagoCant, SantiagoTasa):
    SantiagoR = SantiagoCant * SantiagoTasa
    return SantiagoR

SantiagoDols = 120
SantiagoTasa = 4.9
print(f"La conversión de todos tus dólares es de: ${SantiagoConvDiv(SantiagoDols, SantiagoTasa)}COP")
