class SantiagoB:
    SantiagoGast = []

    def __init__(self, SantiagoDesc, SantiagoCant):
        self.descripcion = SantiagoDesc
        self.cantidad = SantiagoCant
        SantiagoB.SantiagoGast.append({"descripcion": SantiagoDesc, "cantidad": SantiagoCant})

    @classmethod
    def SantiagoMos(cls):
        SantiagoTot = sum([SantiagoG["cantidad"] for SantiagoG in cls.SantiagoGast])
        print("Gastos registrados:", cls.SantiagoGast)
        print("Total gastado:", SantiagoTot)

Santiago1 = SantiagoB("Compra comida", 50)
Santiago2 = SantiagoB("Transporte", 20)
SantiagoB.SantiagoMos()
