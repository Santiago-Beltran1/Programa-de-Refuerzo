class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoPot(self, SantiagoBase, SantiagoExpo):
        return SantiagoBase ** SantiagoExpo

Santiago1 = SantiagoB("Calculador de Potencia")
print(f"4^3 = {Santiago1.SantiagoPot(4,3)}")
