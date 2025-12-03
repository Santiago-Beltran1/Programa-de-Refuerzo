# Analizador de texto
def santiagoContar(texto):
    """Cuenta cuántas palabras hay en un texto"""
    santiagoP = texto.split() 
    return len(santiagoP)

def santiagoCaracteres(texto, santiagoIncEspacio=True):
    """Cuenta los caracteres del texto"""
    if santiagoIncEspacio:
        return len(texto)
    else:
        return len(texto.replace(" ", "")) 
    
def santiagoPMlarga(texto):
    """Encuentra la palabra más larga en el texto"""
    santiagoPs = texto.split()
    santiagoPL = ""

def santiagoPMlarga(santiagoPlbs):
    santiagoPLarga = ""
    for santiagoP in santiagoPlbs:
        if len(santiagoP) > len(santiagoPLarga):
            santiagoPLarga = santiagoP

    return santiagoPLarga

def es_palindromo(SantiagoText):
    """Verifica si un texto es palíndromo (se lee igual al revés)"""
    # Convertir a minúsculas y quitar espacios
    santiagoLimpio = SantiagoText.lower().replace(" ", "")
    santiagoInvert = santiagoLimpio[::-1] # [::-1] invierte el texto
    return santiagoLimpio == santiagoInvert

# Probando el analizador
santiagoFrase = "David Santiago Beltran Pedraza"
print("ANALIZADOR DE TEXTO")
print(f"Texto: '{santiagoFrase}'")
print("-" * 50)
print(f"Palabras: {santiagoContar(santiagoFrase)}")
print(f"Caracteres (con espacios): {santiagoCaracteres(santiagoFrase)}")
print(f"Caracteres (sin espacios): {santiagoCaracteres(santiagoFrase, False)}")
print(f"Palabra más larga: '{santiagoPMlarga(santiagoFrase)}'")
print(f"¿Es palíndromo?: {es_palindromo(santiagoFrase)}")

# Probando con un palíndromo
santiagoPalin = "amo la paloma"
print(f"\nProbando palíndromo: '{santiagoPalin}'")
print(f"¿Es palíndromo?: {es_palindromo(santiagoPalin)}")