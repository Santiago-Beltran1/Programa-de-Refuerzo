class SantiagoB:
    SantiagoCont = []  

    def __init__(self, SantiagoNom, SantiagoTel):
        self.SantiagoNom = SantiagoNom
        self.SantiagoTel = SantiagoTel
        SantiagoB.SantiagoCont.append(self)

    @classmethod
    def SantiagoMos(cls):
        print("Contactos registrados:")
        for SantiagoC in cls.SantiagoCont:
            print(f"{SantiagoC.SantiagoNom} - {SantiagoC.SantiagoTel}")

Santiago1 = SantiagoB("David", "1234567890")
Santiago2 = SantiagoB("Beltran", "1111111111")

SantiagoB.SantiagoMos()
