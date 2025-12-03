class SantiagoBV:
    def __init__(self, SantiagoM, SantiagoModeL):
        self.SantiagoM = SantiagoM
        self.SantiagoModel = SantiagoModeL
        self.SantiagoVel = 0

    def SantiagoAce(self, SantiagoInc):
        if SantiagoInc > 0:
            self.SantiagoVel += SantiagoInc
            return f"{self.SantiagoM} {self.SantiagoModel} aceleró a {self.SantiagoVel} km/h."
        else:
            return "El incremento de velocidad debe ser positivo."

    def SantiagoFreno(self, SantiagoDecr):
        if SantiagoDecr > 0:
            self.SantiagoVel = max(0, self.SantiagoVel - SantiagoDecr)
            return f"{self.SantiagoM} {self.SantiagoModel} frenó a {self.SantiagoVel} km/h."
        else:
            return "El decremento de velocidad debe ser positivo."

    def SantiagoObtV(self):
        return f"Velocidad actual: {self.SantiagoVel} km/h."

SantiagoC1 = SantiagoBV("Nissan", "SR")
print(SantiagoC1.SantiagoAce(70))
print(SantiagoC1.SantiagoAce(10))
print(SantiagoC1.SantiagoObtV())
print(SantiagoC1.SantiagoFreno(20))
print(SantiagoC1.SantiagoFreno(20))
print(SantiagoC1.SantiagoObtV())
