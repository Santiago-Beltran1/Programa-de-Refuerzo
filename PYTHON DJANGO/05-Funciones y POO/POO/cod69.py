class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoProm(self, SantiagoList):
        return sum(SantiagoList)/len(SantiagoList) if SantiagoList else 0

Santiago1 = SantiagoB("Promedio")
print("Promedio:", Santiago1.SantiagoProm([100, 208, 135, 321]))
