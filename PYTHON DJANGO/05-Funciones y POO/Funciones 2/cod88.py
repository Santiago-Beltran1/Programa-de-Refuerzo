class SantiagoHaB:
    def __init__(self, SantiagoNom):
        self.SantiagoNombre = SantiagoNom
        self.SantiagoDias = 0

    def SantiagoRegiS(self):
        self.SantiagoDias += 1
        print(f"SantiagoRegistro de hábito: {self.SantiagoNombre} completado {self.SantiagoDias} días")

SantiagoEj1 = SantiagoHaB("HacerEjercicio")
SantiagoEj1.SantiagoRegiS()
SantiagoEj1.SantiagoRegiS()
