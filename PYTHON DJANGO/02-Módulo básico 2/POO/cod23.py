class SantiagoBFig:
    """Clase base para todas las figuras"""
    def SantiagoArea(self):
        pass

    def SantiagoPerimetro(self):
        pass


class SantiagoCirculo(SantiagoBFig):
    def __init__(self, santiago_radio):
        self.santiago_radio = santiago_radio

    def SantiagoArea(self):
        return 3.1416 * self.santiago_radio ** 2

    def SantiagoPerimetro(self):
        return 2 * 3.1416 * self.santiago_radio


class SantiagoCuadrado(SantiagoBFig):
    def __init__(self, santiago_lado):
        self.santiago_lado = santiago_lado

    def SantiagoArea(self):
        return self.santiago_lado ** 2

    def SantiagoPerimetro(self):
        return 4 * self.santiago_lado


class SantiagoRectangulo(SantiagoBFig):
    def __init__(self, santiago_base, santiago_altura):
        self.santiago_base = santiago_base
        self.santiago_altura = santiago_altura

    def SantiagoArea(self):
        return self.santiago_base * self.santiago_altura

    def SantiagoPerimetro(self):
        return 2 * (self.santiago_base + self.santiago_altura)


class SantiagoTriangulo(SantiagoBFig):
    def __init__(self, santiago_base, santiago_altura, santiago_lado1, santiago_lado2, santiago_lado3):
        self.santiago_base = santiago_base
        self.santiago_altura = santiago_altura
        self.santiago_lado1 = santiago_lado1
        self.santiago_lado2 = santiago_lado2
        self.santiago_lado3 = santiago_lado3

    def SantiagoArea(self):
        return (self.santiago_base * self.santiago_altura) / 2

    def SantiagoPerimetro(self):
        return self.santiago_lado1 + self.santiago_lado2 + self.santiago_lado3


def SantiagoMosFig(figura):
    SantiagoNom = figura.__class__.__name__
    print(f"\n{SantiagoNom}:")
    print(f" Área: {figura.SantiagoArea():.2f}")
    print(f" Perímetro: {figura.SantiagoPerimetro():.2f}")


SantiagoFigs = [
    SantiagoCirculo(7),
    SantiagoCuadrado(6),
    SantiagoRectangulo(8, 4),
    SantiagoTriangulo(5, 6, 5, 6, 7)
]

print("=== CALCULADORA DE FIGURAS SANTIAGO ===")
for SantiagoFig in SantiagoFigs:
    SantiagoMosFig(SantiagoFig)
