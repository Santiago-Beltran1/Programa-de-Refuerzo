class SantiagoB:
    SantiagoAgen = []

    def __init__(self, SantiagoNom, SantiagoTel):
        self.SantiagoNom = SantiagoNom
        self.SantiagoTel = SantiagoTel
        SantiagoB.SantiagoAgen.append(self)

    @classmethod
    def SantiagoBus(cls, SantiagoNom):
        SantiagoR = [SantiagoObj for SantiagoObj in cls.SantiagoAgen if SantiagoNom.lower() in SantiagoObj.SantiagoNom.lower()]
        return SantiagoR

    @classmethod
    def SantiagoMos(cls):
        for SantiagoObj in cls.SantiagoAgen:
            print(f"{SantiagoObj.SantiagoNom} - {SantiagoObj.SantiagoTel}")

# Uso
Santiago1 = SantiagoB("David Beltran", "111111")
Santiago2 = SantiagoB("Santiago Pedraza", "222222")

print("Buscando 'David Beltran':")
for res in SantiagoB.SantiagoBus("David Beltran"):
    print(res.SantiagoNom, res.SantiagoTel)

print("\nTodos los contactos registrados:")
SantiagoB.SantiagoMos()
