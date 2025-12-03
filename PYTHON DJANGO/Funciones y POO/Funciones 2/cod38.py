import re as SantiagoRe

def SantiagoReemp(SantiagoT, SantiagoV, SantiagoNew):
    return SantiagoRe.sub(SantiagoV, SantiagoNew, SantiagoT)

SantiagoF = "Mi nombre completo es David Santiago Beltran Ped"
print(f"Texto Viejo: {SantiagoF}")
print(f"Texto con palabra reemplazada: {SantiagoReemp(SantiagoF, "Ped", "Pedraza")}")
