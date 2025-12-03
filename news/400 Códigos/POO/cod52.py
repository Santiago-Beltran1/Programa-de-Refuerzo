class SantiagoB:
    SantiagoAgenda = []

    def __init__(self, SantiagoNom, SantiagoFecha):
        self.SantiagoNom = SantiagoNom
        self.SantiagoFecha = SantiagoFecha
        SantiagoB.SantiagoAgenda.append(self)

    @classmethod
    def SantiagoMos(cls):
        print("Agenda Santiago de cumpleaños:")
        for SantiagoObj in cls.SantiagoAgenda:
            print(f"{SantiagoObj.SantiagoNom} - {SantiagoObj.SantiagoFecha}")

Santiago1 = SantiagoB("DavidS Beltran", "02/12/2007")
Santiago2 = SantiagoB("Santiago Pedraza", "11/11/2012")
SantiagoB.SantiagoMos()
