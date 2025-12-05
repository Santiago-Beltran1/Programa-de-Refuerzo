import re as SantiagoRe

class SantiagoUser:
    def __init__(self, SantiagoNom, SantiagoEmail):
        self.SantiagoNombre = SantiagoNom
        self.SantiagoEmail = SantiagoEmail

    def SantiagoValidar(self):
        return bool(SantiagoRe.match(r"[^@]+@[^@]+\.[^@]+", self.SantiagoEmail))

SantiagoUser = SantiagoUser("Santiago", "santiago@mail.com")
print(f"EL correo es válido: {SantiagoUser.SantiagoValidar()}")
