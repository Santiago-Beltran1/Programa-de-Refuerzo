import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoLanz(self, SantiagoCant=2, SantiagoCaras=6):
        SantiagoR = [random.randint(1, SantiagoCaras) for _ in range(SantiagoCant)]
        SantiagoSum = sum(SantiagoR)
        return SantiagoR, SantiagoSum

Santiago1 = SantiagoB("DadosSantiago")
SantiagoRes, SantiagoSum = Santiago1.SantiagoLanz(4)
print(f"Resultados: {SantiagoRes} - Suma de todos los resultados de los lanzamientos: {SantiagoSum}")
