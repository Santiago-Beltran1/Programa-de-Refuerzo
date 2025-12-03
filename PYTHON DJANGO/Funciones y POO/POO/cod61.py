import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoAleat(self, SantiagoMin, SantiagoMax):
        return random.randint(SantiagoMin, SantiagoMax)

Santiago1 = SantiagoB("RandomIzer de números")
print("Número aleatorio:", Santiago1.SantiagoAleat(1, 750))
