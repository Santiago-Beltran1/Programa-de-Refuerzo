import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoLanz(self, SantiagoCaras=6):
        return random.randint(1, SantiagoCaras)

Santiago1 = SantiagoB("Randomizer de un dado")
print(f"Resultado del dado: {Santiago1.SantiagoLanz()}")
