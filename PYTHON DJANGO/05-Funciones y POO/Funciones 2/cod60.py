import random as SantiagoRandom

def SantiagoBaraja():
    SantiagoPalos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    SantiagoNums = list(range(1,14))
    SantiagoMazo = [(SantiagoNum, SantiagoPalo) for SantiagoNum in SantiagoNums for SantiagoPalo in SantiagoPalos]
    SantiagoRandom.shuffle(SantiagoMazo)
    return SantiagoMazo

print(f"Cartas que te tocaron: {SantiagoBaraja()[:5]}")
