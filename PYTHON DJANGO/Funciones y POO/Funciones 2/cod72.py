class SantiagoT:
    def __init__(self, SantiagoDesc, SantiagoEstado="pendiente"):
        self.SantiagoDescripcion = SantiagoDesc
        self.SantiagoEstado = SantiagoEstado

class SantiagoRep:
    def __init__(self):
        self.SantiagoT = []

    def SantiagoAg(self, SantiagoTareaItem):
        self.SantiagoT.append(SantiagoTareaItem)

    def SantiagoGen(self):
        SantiagoReporte = {}
        for t in self.SantiagoT:
            SantiagoReporte[t.SantiagoDescripcion] = t.SantiagoEstado
        return SantiagoReporte

Santiago1 = SantiagoRep()
Santiago1.SantiagoAg(SantiagoT("Backend", "hecha"))
Santiago1.SantiagoAg(SantiagoT("Frontend", "pendiente"))
print(Santiago1.SantiagoGen())
