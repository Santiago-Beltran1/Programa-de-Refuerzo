class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoCalIMC(self, SantiagoPeso, SantiagoAltura):
        SantiagoIMC = SantiagoPeso / (SantiagoAltura ** 2)
        return SantiagoIMC

    def SantiagoCateg(self, SantiagoIMC):
        if SantiagoIMC < 18.5:
            return "Bajo peso"
        elif SantiagoIMC < 25:
            return "Normal"
        elif SantiagoIMC < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"

# Uso
Santiago1 = SantiagoB("IMC")
SantiagoIMC = Santiago1.SantiagoCalIMC(63, 1.71)
print("IMC de la persona: ", SantiagoIMC)
print("Categoría:", Santiago1.SantiagoCateg(SantiagoIMC))
