import string

def SantiagoBSeguridad(SantiagoBClave):
    SantiagoBLongitud = len(SantiagoBClave) >= 8
    SantiagoBMayus = any(c.isupper() for c in SantiagoBClave)
    SantiagoBMinus = any(c.islower() for c in SantiagoBClave)
    SantiagoBNumeros = any(c.isdigit() for c in SantiagoBClave)
    SantiagoBSimbolos = any(c in string.punctuation for c in SantiagoBClave)
    return all([SantiagoBLongitud, SantiagoBMayus, SantiagoBMinus, SantiagoBNumeros, SantiagoBSimbolos])

SantiagoBClave = input("Ingresa una contraseña: ")
print("Contraseña segura" if SantiagoBSeguridad(SantiagoBClave) else "Contraseña débil")
