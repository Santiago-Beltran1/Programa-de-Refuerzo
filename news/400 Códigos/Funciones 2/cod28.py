def SantiagoCuadDic(SantiagoLimit):
    return {SantiagoN: SantiagoN**2 for SantiagoN in range(1, SantiagoLimit+1)}

print(f"Cuadrado de cada número hasta el 7: {SantiagoCuadDic(7)}")
