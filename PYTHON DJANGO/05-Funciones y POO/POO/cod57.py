import random
import string

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoGen(self, SantiagoLong):
        SantiagoChars = string.ascii_letters + string.digits + string.punctuation
        SantiagoContras = ''.join(random.choice(SantiagoChars) for _ in range(SantiagoLong))
        return SantiagoContras

Santiago1 = SantiagoB("GeneradorSantiago")
print("Contraseña Santiago:", Santiago1.SantiagoGen(10))
