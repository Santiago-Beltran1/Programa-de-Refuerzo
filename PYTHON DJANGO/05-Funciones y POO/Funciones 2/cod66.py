import random as SantiagoRandom
import string as SantiagoString

def SantiagoArch(SantiagoNom, SantiagoLin):
    with open(SantiagoNom, "w") as SantiagoF:
        for _ in range(SantiagoLin):
            SantiagoLinea = ''.join(SantiagoRandom.choices(SantiagoString.ascii_letters + " ", k=50))
            SantiagoF.write(SantiagoLinea + "\n")
    return f"{SantiagoNom} creado"

print(SantiagoArch("SantiagoTexto.txt", 5))
