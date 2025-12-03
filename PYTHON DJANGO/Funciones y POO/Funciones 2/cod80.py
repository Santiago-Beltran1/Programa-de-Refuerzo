import random as SantiagoRandom

def SantiagoGenNom(SantiagoCant):
    SantiagoPrefijos = ["Auto", "Mega", "Pro", "Ultra"]
    SantiagoSufijos = ["Sys", "Tools", "Lab", "App"]
    for _ in range(SantiagoCant):
        SantiagoNom = SantiagoRandom.choice(SantiagoPrefijos) + SantiagoRandom.choice(SantiagoSufijos)
        print(f"SantiagoNombre de proyecto generado: {SantiagoNom}")

SantiagoGenNom(4)
