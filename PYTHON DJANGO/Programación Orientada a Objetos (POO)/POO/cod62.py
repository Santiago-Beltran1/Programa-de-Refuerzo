class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoCOPaUSD(self, SantiagoCOP, SantiagoTasa):
        return SantiagoCOP / SantiagoTasa

    def SantiagoUSDtoCOP(self, SantiagoUSD, SantiagoTasa):
        return SantiagoUSD * SantiagoTasa

Santiago1 = SantiagoB("Moneda Cambio")
SantiagoTasa = 5000 
print("50000 COP a USD:", Santiago1.SantiagoCOPaUSD(50000, SantiagoTasa))
print("30 USD a COP:", Santiago1.SantiagoUSDtoCOP(30, SantiagoTasa))
