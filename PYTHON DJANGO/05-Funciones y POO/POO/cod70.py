import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoMon(self):
        SantiagoR = random.choice(["Sale Cara", "Sale Cruz"])
        return SantiagoR

Santiago1 = SantiagoB("Lanzamiento de mondeda")
print("Lanzamiento:", Santiago1.SantiagoMon())
