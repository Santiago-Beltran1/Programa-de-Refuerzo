class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoMaH(self, SantiagoMins):
        SantiagoH = SantiagoMins // 60
        SantiagoMin = SantiagoMins % 60
        return SantiagoH, SantiagoMin

Santiago1 = SantiagoB("Conversor de Minutos a Horas")
SantiagoHD, SantiagoMD = Santiago1.SantiagoMaH(100)
print(f"100 minutos = {SantiagoHD} horas y {SantiagoMD} minutos")
