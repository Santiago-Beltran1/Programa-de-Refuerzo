class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoIS(self, SantiagoCapi, SantiagoTasa, SantiagoTiempo):
        return SantiagoCapi * SantiagoTasa * SantiagoTiempo / 100

Santiago1 = SantiagoB("Interes Compuesto Calcular")
print(f"Interés simple: {Santiago1.SantiagoIS(3000000, 4, 3)}")
