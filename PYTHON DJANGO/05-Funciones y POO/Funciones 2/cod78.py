class SantiagoVot:
    def __init__(self, SantiagoOpc):
        self.SantiagoOpciones = {op:0 for op in SantiagoOpc}

    def SantiagoVotar(self, SantiagoOpcion):
        if SantiagoOpcion in self.SantiagoOpciones:
            self.SantiagoOpciones[SantiagoOpcion] += 1
            print(f"Voto registrado para: {SantiagoOpcion}")
        else:
            print(f"Opción inválida: {SantiagoOpcion}")

    def SantiagoR(self):
        print("Resultados de la votación:")
        for SantiagoK,SantiagoB in self.SantiagoOpciones.items():
            print(f"  {SantiagoK}: {SantiagoB} votos")

SantiagoV = SantiagoVot(["Nacional", "Millos", "Cali"])
SantiagoV.SantiagoVotar("Millos")
SantiagoV.SantiagoVotar("Millos")
SantiagoV.SantiagoVotar("Cali")
SantiagoV.SantiagoR()
