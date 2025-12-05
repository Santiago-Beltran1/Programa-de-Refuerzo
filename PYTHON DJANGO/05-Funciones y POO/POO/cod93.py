class SantiagoB:
    def __init__(self, SantiagoAlumno):
        self.SantiagoAlumn = SantiagoAlumno
        self.SantiagoNotas = []

    def SantiagoAg(self, SantiagoNota):
        self.SantiagoNotas.append(SantiagoNota)

    def SantiagoA(self):
        SantiagoProm = sum(self.SantiagoNotas)/len(self.SantiagoNotas) if self.SantiagoNotas else 0
        return SantiagoProm >= 3

Santiago1 = SantiagoB("David")
Santiago1.SantiagoAg(4.0)
Santiago1.SantiagoAg(2.0)
print(f"Aprobado: {Santiago1.SantiagoA()}")
