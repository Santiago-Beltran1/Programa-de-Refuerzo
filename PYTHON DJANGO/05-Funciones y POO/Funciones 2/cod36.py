import random as SantiagoRandom
import string as SantiagoString

def SantiagoCadAle(SantiagoLong):
    SantiagoCaract = SantiagoString.ascii_letters + SantiagoString.digits
    return ''.join(SantiagoRandom.choice(SantiagoCaract) for _ in range(SantiagoLong))

print(f"Nueva cadena de texto: {SantiagoCadAle(20)}")
