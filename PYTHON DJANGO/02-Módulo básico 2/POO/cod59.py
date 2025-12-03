class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoCont(self, SantiagoTex):
        SantiagoP = SantiagoTex.split()
        return len(SantiagoP)

Santiago1 = SantiagoB("Contador de Palabras")
SantiagoTexto = "David Santiago Beltran Pedraza"
print("Número de palabras:", Santiago1.SantiagoCont(SantiagoTexto))
