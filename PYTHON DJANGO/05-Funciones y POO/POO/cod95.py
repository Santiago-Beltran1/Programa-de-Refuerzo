import random
import string

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoGenPass(self, SantiagoLong=12, SantiagoMayus=True, SantiagoNums=True, SantiagoSimbolos=True):
        SantiagoChars = string.ascii_lowercase
        if SantiagoMayus:
            SantiagoChars += string.ascii_uppercase
        if SantiagoNums:
            SantiagoChars += string.digits
        if SantiagoSimbolos:
            SantiagoChars += "!@#$%^&*()"
        SantiagoContra = ''.join(random.choice(SantiagoChars) for _ in range(SantiagoLong))
        return SantiagoContra

Santiago1 = SantiagoB("Generador de contraseña")
print(f"Contraseña generada: {Santiago1.SantiagoGenPass(16)}")
