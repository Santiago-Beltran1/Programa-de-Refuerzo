class SantiagoB:
    SantiagoRegis = []

    def __init__(self, Santiago):
        self.Santiago = Santiago
        SantiagoB.SantiagoRegis.append(Santiago)

    @classmethod
    def SantiagoEli(cls, SantiagoNom):
        if SantiagoNom in cls.SantiagoRegis:
            cls.SantiagoRegis.remove(SantiagoNom)
            print(f"{SantiagoNom} eliminado.")
        else:
            print(f"{SantiagoNom} no encontrado.")

Santiago1 = SantiagoB("David")
Santiago2 = SantiagoB("Beltran")

SantiagoB.SantiagoEli("David")
SantiagoB.SantiagoEli("Santiago")
print(SantiagoB.SantiagoRegis)
