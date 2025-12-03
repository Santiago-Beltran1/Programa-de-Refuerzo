class SantiagoN:
    def __init__(self):
        self.SantiagoNotas = []

    def SantiagoAg(self, SantiagoTexto):
        self.SantiagoNotas.append(SantiagoTexto)
        print(f"Nota agregada: {SantiagoTexto}")

    def SantiagoBus(self, SantiagoP):
        SantiagoR = [SantiagoN for SantiagoN in self.SantiagoNotas if SantiagoP.lower() in SantiagoN.lower()]
        if SantiagoR:
            print(f"Notas encontradas con '{SantiagoP}': {SantiagoR}")
        else:
            print(f"No se encontraron notas con '{SantiagoP}'")

Santiago1 = SantiagoN()
Santiago1.SantiagoAg("Django")
Santiago1.SantiagoAg("Proyecto ")
Santiago1.SantiagoBus("GYM")
