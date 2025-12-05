def SantiagoB(*SantiagoN):
    SantiagoTot = 0
    for Santiagonum in SantiagoN:
        SantiagoTot += Santiagonum
    return SantiagoTot

Santiago1 = SantiagoB(12, 32)
Santiago2 = SantiagoB(10, 20, 30, 40, 50)

print(f"El resultado de la suma entre todos los números es: {Santiago1}")  
print(f"El resultado de la suma entre todos los números es: {Santiago2}")  
