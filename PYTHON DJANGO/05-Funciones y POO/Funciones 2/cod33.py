import random as SantiagoRandom

def SantiagoNumU(SantiagoCant, SantiagoMax):
    return SantiagoRandom.sample(range(1, SantiagoMax+1), SantiagoCant)

print(f"Números que salen de el randomizer: {SantiagoNumU(3, 17)}")
