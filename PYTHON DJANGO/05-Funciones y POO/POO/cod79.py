class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoContD(self, SantiagoN):
        return len(str(abs(SantiagoN)))

Santiago1 = SantiagoB("Contador de dígitos")
print("Número de dígitos:", Santiago1.SantiagoContD(12345))
