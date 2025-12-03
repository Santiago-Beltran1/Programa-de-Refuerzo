import string as SantiagoString
import random as SantiagoRandom

def SantiagoGen(SantiagoLongitud):
    SantiagoCaract = SantiagoString.ascii_letters + SantiagoString.digits + SantiagoString.punctuation
    SantiagoPassword = ''.join(SantiagoRandom.choices(SantiagoCaract, k=SantiagoLongitud))
    return SantiagoPassword

print(SantiagoGen(16))
