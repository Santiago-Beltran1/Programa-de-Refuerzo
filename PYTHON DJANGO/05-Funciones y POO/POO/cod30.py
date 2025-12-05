class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def saludarSantiago(self):
        print(f"Hola desde Santiago")

class SantiagoSon(SantiagoB):
    def saludarSantiago(self):
        print(f"Hola desde HijoSantiago")

Santiago1 = SantiagoSon("Santiago")
Santiago1.saludarSantiago()
Santiago2 = SantiagoB("Santiago")
Santiago2.saludarSantiago()