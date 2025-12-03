import random as SantiagoRandom

def SantiagoCols(SantiagoCant):
    return ["#"+''.join(SantiagoRandom.choices("0123456789ABCDEF", k=6)) for _ in range(SantiagoCant)]

print(f"Colores recomendados para probar: {SantiagoCols(5)}")
