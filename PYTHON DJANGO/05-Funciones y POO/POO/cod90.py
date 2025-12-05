class SantiagoBC:
    def __init__(self, SantiagoNom, SantiagoSaldo=0):
        self.SantiagoNom = SantiagoNom
        self.SantiagoSaldo = SantiagoSaldo

    def SantiagoDep(self, SantiagoCant):
        self.SantiagoSaldo += SantiagoCant

    def SantiagoRet(self, SantiagoCant):
        if SantiagoCant <= self.SantiagoSaldo:
            self.SantiagoSaldo -= SantiagoCant
        else:
            print(f"{self.SantiagoNom}: Saldo insuficiente para retirar {SantiagoCant}")

    def SantiagoTrans(self, SantiagoDest, SantiagoCant):
        if SantiagoCant <= self.SantiagoSaldo:
            self.SantiagoRet(SantiagoCant)
            SantiagoDest.SantiagoDep(SantiagoCant)
            print(f"Transferencia realizada: {self.SantiagoNom} transfirió {SantiagoCant} a {SantiagoDest.SantiagoNom}")
        else:
            print(f"{self.SantiagoNom}: No hay saldo suficiente para transferir {SantiagoCant}")

Santiago1 = SantiagoBC("David", 150000)
Santiago2 = SantiagoBC("Santiago", 25000)

Santiago1.SantiagoTrans(Santiago2, 40000)

print(f"Saldo final: {Santiago1.SantiagoNom}: {Santiago1.SantiagoSaldo}, {Santiago2.SantiagoNom}: {Santiago2.SantiagoSaldo}")
