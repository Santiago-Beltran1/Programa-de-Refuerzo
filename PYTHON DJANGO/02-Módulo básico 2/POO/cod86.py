class SantiagoB:
    def __init__(self, SantiagoAlumn):
        self.SantiagoAlumnN = SantiagoAlumn
        self.SantiagoNotas = []

    def SantiagoAgNota(self, SantiagoNota):
        self.SantiagoNotas.append(SantiagoNota)

    def SantiagoProm(self):
        return sum(self.SantiagoNotas)/len(self.SantiagoNotas) if self.SantiagoNotas else 0

Santiago1 = SantiagoB("David Beltran")
Santiago1.SantiagoAgNota(3.2)
Santiago1.SantiagoAgNota(1.5)
Santiago1.SantiagoAgNota(4.8)
print(f"Promedio de todas las notas agregadas: {Santiago1.SantiagoProm()}")
