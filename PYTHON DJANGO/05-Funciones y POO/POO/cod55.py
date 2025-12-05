class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoCaF(self, SantiagoC):
        return (SantiagoC * 9/5) + 32

    def SantiagoFaC(self, SantiagoF):
        return (SantiagoF - 32) * 5/9

Santiago1 = SantiagoB("Conversor de Temperatura")
print("25°C a F:", Santiago1.SantiagoCaF(21))
print("77°F a C:", Santiago1.SantiagoFaC(45))
