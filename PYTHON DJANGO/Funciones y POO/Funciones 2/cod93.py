class SantiagoG:
    def __init__(self):
        self.SantiagoGastos = []

    def SantiagoAg(self, SantiagoDesc, SantiagoMonto):
        self.SantiagoGastos.append({"descripcion":SantiagoDesc,"monto":SantiagoMonto})
        print(f"Gasto agregado: {SantiagoDesc} - ${SantiagoMonto}")

    def SantiagoTot(self):
        SantiagoTotal = sum(SantiagoG["monto"] for SantiagoG in self.SantiagoGastos)
        print(f"Total de gastos: ${SantiagoTotal}")

SantiagoG = SantiagoG()
SantiagoG.SantiagoAg("Comida", 300000)
SantiagoG.SantiagoAg("Recibos",300000)
SantiagoG.SantiagoTot()
