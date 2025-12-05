import random as SantiagoRandom

def SantiagoLanz(SantiagoVeces):
    return [SantiagoRandom.choice(["SaleCara", "SaleCruz"]) for _ in range(SantiagoVeces)]

print(SantiagoLanz(8))
