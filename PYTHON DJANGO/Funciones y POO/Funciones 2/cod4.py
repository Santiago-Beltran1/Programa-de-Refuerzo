import random
import string

def SantiagoContra(SantiagoLong):
    SantiagoCarac = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(SantiagoCarac) for _ in range(SantiagoLong))

print(f"Contraseña que se creo: {SantiagoContra(10)}")
