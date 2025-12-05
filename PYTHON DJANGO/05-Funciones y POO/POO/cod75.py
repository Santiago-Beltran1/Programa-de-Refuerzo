class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoVel(self, SantiagoDist, SantiagoTiempo):
        return SantiagoDist / SantiagoTiempo if SantiagoTiempo != 0 else 0

Santiago1 = SantiagoB("Calculador de Velocidad")
print("Velocidad:", Santiago1.SantiagoVel(90, 3), "m/s")
