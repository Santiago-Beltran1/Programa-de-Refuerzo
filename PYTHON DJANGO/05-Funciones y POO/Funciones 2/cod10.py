class SantiagoTarea:
    def __init__(self, SantiagoNomb):
        self.SantiagoNom = SantiagoNomb
        self.SantiagoCompletada = False

    def SantiagoCompletar(self):
        self.SantiagoCompletada = True

class SantiagoList:
    def __init__(self):
        self.SantiagoT = []

    def SantiagoAg(self, tarea):
        self.SantiagoT.append(tarea)

    def SantiagoMosPend(self):
        return [t.SantiagoNom for t in self.SantiagoT if not t.SantiagoCompletada]

Santiago1 = SantiagoTarea("Hacer el almuerzo")
Santiago2 = SantiagoTarea("Hacer los 400 ejercicios")
SantiagoL = SantiagoList()
SantiagoL.SantiagoAg(Santiago1)
SantiagoL.SantiagoAg(Santiago2)
Santiago1.SantiagoCompletar()
print(SantiagoL.SantiagoMosPend())
