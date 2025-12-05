import random as SantiagoRandom
import string as SantiagoString

def SantiagoCodPr(SantiagoLong):
    SantiagoCod = ''.join(SantiagoRandom.choices(SantiagoString.ascii_uppercase + SantiagoString.digits, k=SantiagoLong))
    return SantiagoCod

print(f"Código de Paquete de Lenteja: {SantiagoCodPr(8)}")
print(f"Código de Gaseosa: {SantiagoCodPr(8)}")
print(f"Código de Paquete de Maiz: {SantiagoCodPr(8)}")

