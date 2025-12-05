import random

def SantiagoAdiv():
    SantiagoNSecreto = random.randint(1, 50)
    SantiagoInten = 0
    SantiagoAdivinado = False
    while not SantiagoAdivinado:
        SantiagoInten += 1
        SantiagoIntento = random.randint(1, 50)
        if SantiagoIntento == SantiagoNSecreto:
            SantiagoAdivinado = True
    return SantiagoInten

print(SantiagoAdiv())
