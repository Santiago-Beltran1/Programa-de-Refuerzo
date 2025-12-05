class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoAC(self, SantiagoLado):
        return SantiagoLado ** 2

    def SantiagoAR(self, SantiagoBase, SantiagoAltura):
        return SantiagoBase * SantiagoAltura

    def SantiagoAC(self, SantiagoRadio):
        import math
        return math.pi * SantiagoRadio ** 2

Santiago1 = SantiagoB("AreaSantiago")
print(f"Área Cuadrado = {Santiago1.SantiagoAC(7)}")
print(f"Área Rectángulo  = { Santiago1.SantiagoAR(12,4)}")
print(f"Área Círculo  = { Santiago1.SantiagoAC(3)}")
