import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoClima(self):
        SantiagoClimas = ["Soleado", "Nublado", "Lluvioso", "Tormenta", "Templado"]
        return random.choice(SantiagoClimas)

Santiago1 = SantiagoB("Clima")
print("Clima actual:", Santiago1.SantiagoClima())
