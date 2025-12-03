import random
import string

def SantiagoBGenerarClave(SantiagoLongitud=12):
    SantiagoCaracteres = string.ascii_letters + string.digits + "!@#$%^&*()?"
    return ''.join(random.choice(SantiagoCaracteres) for _ in range(SantiagoLongitud))

print("Contraseña generada:", SantiagoBGenerarClave())
