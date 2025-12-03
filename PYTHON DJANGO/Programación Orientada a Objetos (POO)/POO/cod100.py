class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoMedia(self, SantiagoList):
        return sum(SantiagoList)/len(SantiagoList) if SantiagoList else 0

    def SantiagoMax(self, SantiagoLista):
        return max(SantiagoLista) if SantiagoLista else None

    def SantiagoMin(self, SantiagoLista):
        return min(SantiagoLista) if SantiagoLista else None

Santiago1 = SantiagoB("Estadísticas de una lista de números")
SantiagoN = [44, 48, 48, 24]
print(f"Media: {Santiago1.SantiagoMedia(SantiagoN)}")
print(f"Máximo: {Santiago1.SantiagoMax(SantiagoN)}")
print(f"Mínimo: {Santiago1.SantiagoMin(SantiagoN)}")