def SantiagoCalcularIMC(SantiagoPeso, SantiagoAltura):
    return SantiagoPeso / (SantiagoAltura ** 2)

print(f"Su condición IMC si pesará 80kg y midiera 1.60m sería de: {SantiagoCalcularIMC(80, 1.60)}")
