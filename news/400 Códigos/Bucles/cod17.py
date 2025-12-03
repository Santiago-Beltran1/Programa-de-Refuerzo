def SantiagoBFacto(SantiagoN):
    SantiagoR = 1
    while SantiagoN > 0:
        SantiagoR *= SantiagoN
        SantiagoN -= 1
    return SantiagoR
print(f"El factorial de 10 es igual a: {SantiagoBFacto(10)}")