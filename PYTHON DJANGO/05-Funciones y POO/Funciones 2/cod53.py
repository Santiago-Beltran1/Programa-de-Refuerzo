class SantiagoInv:
    def __init__(self):
        self.SantiagoProds = {}

    def SantiagoAgP(self, SantiagoNom, SantiagoCant):
        if SantiagoNom in self.SantiagoProds:
            self.SantiagoProds[SantiagoNom] += SantiagoCant
        else:
            self.SantiagoProds[SantiagoNom] = SantiagoCant

    def SantiagoTotalP(self):
        return sum(self.SantiagoProds.values())

Santiago1 = SantiagoInv()
Santiago1.SantiagoAgP("Sudadera", 12)
Santiago1.SantiagoAgP("Gorra", 7)
print(f"El total de productos guardados en el inventario es de: {Santiago1.SantiagoTotalP()} unidades")
