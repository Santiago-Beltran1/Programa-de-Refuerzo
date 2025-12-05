import re

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoSeguro(self, SantiagoContras):
        if (len(SantiagoContras) >= 8 and 
            re.search(r"[A-Z]", SantiagoContras) and 
            re.search(r"[a-z]", SantiagoContras) and 
            re.search(r"[0-9]", SantiagoContras) and 
            re.search(r"[!@#$%^&*]", SantiagoContras)):
            return True
        return False

Santiago1 = SantiagoB("Seguridad de una Contraseña")
print(f"Contraseña segura: {Santiago1.SantiagoSeguro("David12345!")}")
print(f"Contraseña segura: {Santiago1.SantiagoSeguro("holas123")}")
