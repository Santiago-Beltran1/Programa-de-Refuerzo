class SantiagoB:
    def __init__(self, SantiagoSaldo):
        self.SantiagoSaldo = SantiagoSaldo

    def SantiagoDep(self, SantiagoCant):
        self.SantiagoSaldo += SantiagoCant
        print(f"Depositado: {SantiagoCant}, Saldo actual: {self.SantiagoSaldo}")

    def SantiagoRet(self, SantiagoCant):
        if SantiagoCant <= self.SantiagoSaldo:
            self.SantiagoSaldo -= SantiagoCant
            print(f"Retirado: {SantiagoCant}, Saldo actual: {self.SantiagoSaldo}")
        else:
            print("Saldo Santiago insuficiente")

Santiago1 = SantiagoB(2000000)
Santiago1.SantiagoDep(750000)
Santiago1.SantiagoRet(100000)
Santiago1.SantiagoRet(400000)
