class SantiagoB:
    SantiagoRegis = []

    def __init__(self, Santiago):
        self.Santiago = Santiago
        SantiagoB.SantiagoRegis.append(Santiago)

    @classmethod
    def buscarSantiago(cls, nombre):
        if nombre in cls.SantiagoRegis:
            print(f"{nombre} está registrado.")
        else:
            print(f"{nombre} no se encuentra registrado.")

Santiago1 = SantiagoB("David")
Santiago2 = SantiagoB("Beltran")

SantiagoB.buscarSantiago("David")
SantiagoB.buscarSantiago("Santiago")
