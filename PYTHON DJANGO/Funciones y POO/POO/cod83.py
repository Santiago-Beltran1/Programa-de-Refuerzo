class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoSegaHMS(self, SantiagoSeg):
        SantiagoHoras = SantiagoSeg // 3600
        SantiagoMins = (SantiagoSeg % 3600) // 60
        SantiagoSeg = SantiagoSeg % 60
        return SantiagoHoras, SantiagoMins, SantiagoSeg

Santiago1 = SantiagoB("Segundos a Horas Minutos y Segundos")
SantiagoHD, SantiagoMD, SantiagoSD = Santiago1.SantiagoSegaHMS(3671)
print(f"3834 segundos = {SantiagoHD} horas, {SantiagoMD} minutos y {SantiagoSD} segundos")
