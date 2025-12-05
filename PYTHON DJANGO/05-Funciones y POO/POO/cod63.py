class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoApDesc(self, SantiagoCosto, SantiagoDesc):
        SantiagoFinal = SantiagoCosto * (1 - SantiagoDesc/100)
        return SantiagoFinal

Santiago1 = SantiagoB("Aplicador de Descuento")
print("Precio final:", Santiago1.SantiagoApDesc(250000, 15))
