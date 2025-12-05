import random as SantiagoRandom

def SantiagoGen(SantiagoCant):
    SantiagoExtns = [".com", ".net", ".org", ".io"]
    for _ in range(SantiagoCant):
        SantiagoNom = "".join(SantiagoRandom.choices("abcdefghijklmnopqrstuvwxyz", k=7))
        SantiagoDominio = SantiagoNom + SantiagoRandom.choice(SantiagoExtns)
        print(f"Dominio generado: {SantiagoDominio}")

SantiagoGen(5)
