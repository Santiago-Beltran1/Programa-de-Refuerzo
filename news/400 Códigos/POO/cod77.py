class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoKmaMi(self, SantiagoKm):
        return SantiagoKm * 0.621371

Santiago1 = SantiagoB("Conversor KM A MI")
print(f"55 km a millas: {Santiago1.SantiagoKmaMi(55)}")
