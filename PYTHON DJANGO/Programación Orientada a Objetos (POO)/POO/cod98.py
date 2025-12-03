import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoLoter(self, SantiagoNApostados, SantiagoMax=49):
        SantiagoGana = random.sample(range(1, SantiagoMax+1), len(SantiagoNApostados))
        SantiagoAcierto = len(set(SantiagoNApostados) & set(SantiagoGana))
        return SantiagoGana, SantiagoAcierto

Santiago1 = SantiagoB("LoteriaSantiago")
SantiagoWins, SantiagoAcer = Santiago1.SantiagoLoter([5,4,48,15,21,16])
print("Números ganadores:", SantiagoWins, "Aciertos:", SantiagoAcer)
