import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoColRan(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

Santiago1 = SantiagoB("Randomizer de colores")
print(f"Color aleatorio: {Santiago1.SantiagoColRan()}")
