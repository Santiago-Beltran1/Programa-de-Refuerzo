class SantiagoB:
    SantiagoContras = {}

    def __init__(self, SantiagoSitio, SantiagoContrasena):
        self.SantiagoSitio = SantiagoSitio
        self.SantiagoContrasena = SantiagoContrasena
        SantiagoB.SantiagoContras[SantiagoSitio] = SantiagoContrasena

    @classmethod
    def SantiagoMos(cls):
        print("Contraseñas Santiago registradas:")
        for SantiagoSitio, SantiagoContrasena in cls.SantiagoContras.items():
            print(f"{SantiagoSitio} - {SantiagoContrasena}")

Santiago1 = SantiagoB("GmailSantiago", "1234Santiago")
Santiago2 = SantiagoB("FacebookSantiago", "abcdSantiago")
SantiagoB.SantiagoMos()
