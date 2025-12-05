class SantiagoBCB:
    def __init__(self, SantiagoSI=0):
        self.SantiagoSaldo = SantiagoSI

    def SantiagoDep(self, SantiagoCant):
        if SantiagoCant > 0:
            self.SantiagoSaldo += SantiagoCant
            return f"Depósito de {SantiagoCant} realizado. Nuevo saldo: {self.SantiagoSaldo}"
        else:
            return "La cantidad a depositar debe ser positiva."

    def SantiagoRet(self, SantiagoCant):
        if SantiagoCant <= 0:
            return "La cantidad a retirar debe ser positiva."
        if self.SantiagoSaldo >= SantiagoCant:
            self.SantiagoSaldo -= SantiagoCant
            return f"Retiro de {SantiagoCant} realizado. Nuevo saldo: {self.SantiagoSaldo}"
        else:
            return "Saldo insuficiente."

    def SantiagoConsultarSaldo(self):
        return f"Saldo actual: {self.SantiagoSaldo}"

SantiagoCuenta = SantiagoBCB(1500000)
print(SantiagoCuenta.SantiagoConsultarSaldo())
print(SantiagoCuenta.SantiagoDep(200000))
print(SantiagoCuenta.SantiagoRet(500000))
print(SantiagoCuenta.SantiagoRet(100000))
print(SantiagoCuenta.SantiagoConsultarSaldo())
