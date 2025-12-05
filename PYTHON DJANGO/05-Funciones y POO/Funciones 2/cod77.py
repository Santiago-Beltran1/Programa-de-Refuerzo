class SantiagoReu:
    def __init__(self, SantiagoNom):
        self.SantiagoNombre = SantiagoNom
        self.SantiagoPart = []

    def SantiagoAg(self, SantiagoNomP):
        self.SantiagoPart.append(SantiagoNomP)
        print(f"Participante agregado: {SantiagoNomP} a la reunión {self.SantiagoNombre}")

    def SantiagoListP(self):
        print(f"SantiagoParticipantes de {self.SantiagoNombre}: {', '.join(self.SantiagoPart)}")

Santiago1 = SantiagoReu("Proyecto Django")
Santiago1.SantiagoAg("David")
Santiago1.SantiagoAg("Santiago")
Santiago1.SantiagoListP()
