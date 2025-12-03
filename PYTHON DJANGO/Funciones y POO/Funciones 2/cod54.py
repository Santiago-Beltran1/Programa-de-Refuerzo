class SantiagoG:
    def __init__(self, SantiagoDesc, SantiagoMont):
        self.SantiagoDescripcion = SantiagoDesc
        self.SantiagoMonto = SantiagoMont

class SantiagoRegis:
    def __init__(self):
        self.SantiagoGastos = []

    def SantiagoAg(self, SantiagoGastoItem):
        self.SantiagoGastos.append(SantiagoGastoItem)

    def SantiagoTotalGastado(self):
        return sum(g.SantiagoMonto for g in self.SantiagoGastos)

SantiagoR1 = SantiagoRegis()
SantiagoR1.SantiagoAg(SantiagoG("Mercado", 400000))
SantiagoR1.SantiagoAg(SantiagoG("Transporte", 150000))
print(f"El total definitivo sumando todos los gastos es de: ${SantiagoR1.SantiagoTotalGastado()}")
