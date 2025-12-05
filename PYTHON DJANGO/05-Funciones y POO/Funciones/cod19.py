# Usando una función normal
def SantiagoCuadra(SantiagoX):
    return SantiagoX ** 2

SantiagoR = SantiagoCuadra(100)
print(SantiagoR)  

# Usando una función lambda
SantiagoCuadra = lambda SantiagoY: SantiagoY ** 2
SantiagoR = SantiagoCuadra(16)
print(SantiagoR)  