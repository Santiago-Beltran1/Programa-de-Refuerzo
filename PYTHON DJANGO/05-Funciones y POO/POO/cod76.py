class SantiagoB:
    SantiagoTemp = []

    def __init__(self, SantiagoDia, SantiagoTempDia):
        self.SantiagoDia = SantiagoDia
        self.SantiagoTempDia = SantiagoTempDia
        SantiagoB.SantiagoTemp.append(self)

    @classmethod
    def SantiagoMos(cls):
        for SantiagoObj in cls.SantiagoTemp:
            print(f"{SantiagoObj.SantiagoDia}: {SantiagoObj.SantiagoTempDia}°C")

Santiago1 = SantiagoB("Jueves", 19)
Santiago2 = SantiagoB("Martes", 22)
SantiagoB.SantiagoMos()
