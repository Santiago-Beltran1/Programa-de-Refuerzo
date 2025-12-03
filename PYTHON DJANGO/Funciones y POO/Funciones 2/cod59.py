class SantiagoEstudiante:
    def __init__(self, SantiagoNom):
        self.SantiagoNombre = SantiagoNom
        self.SantiagoNotas = []

    def SantiagoAg(self, SantiagoNota):
        self.SantiagoNotas.append(SantiagoNota)

    def SantiagoPromedio(self):
        return sum(self.SantiagoNotas)/len(self.SantiagoNotas) if self.SantiagoNotas else 0

Santiago1 = SantiagoEstudiante("Santiago")
Santiago1.SantiagoAg(47)
Santiago1.SantiagoAg(94)
Santiago1.SantiagoAg(77)
print(f"Promedio del estudiante: {Santiago1.SantiagoPromedio()}")
