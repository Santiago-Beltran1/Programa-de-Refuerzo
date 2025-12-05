class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoCont(self, SantiagoTex):
        SantiagoV = "aeiouAEIOU"
        SantiagoCont = sum(1 for SantiagoC in SantiagoTex if SantiagoC in SantiagoV)
        return SantiagoCont

Santiago1 = SantiagoB("Contador de vocales")
print(f"Número de vocales en el texto: { Santiago1.SantiagoCont("David Santiago Beltran Pedraza")}")
