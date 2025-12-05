class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoHaMaS(self, SantiagoHoras):
        SantiagoMins = SantiagoHoras * 60
        SantiagoSeg = SantiagoMins * 60
        return SantiagoMins, SantiagoSeg

Santiago1 = SantiagoB("ConversorHorasSantiago")
SantiagoM, SantiagoS = Santiago1.SantiagoHaMaS(2)
print(f"2 horas = {SantiagoM} minutos  = {SantiagoS} segundos")
