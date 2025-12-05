class SantiagoB:
    def __init__(self, SantiagoV):
        self.SantiagoV = SantiagoV

    def __add__(self, SantiagoOtro):
        return SantiagoB(self.SantiagoV + SantiagoOtro.SantiagoV)

    def mostrarSantiago(self):
        print(f"Valor de los do números de cada operador: {self.SantiagoV}")

Santiago1 = SantiagoB(17)
Santiago2 = SantiagoB(5)
Santiago3 = Santiago1 + Santiago2
Santiago3.mostrarSantiago()
