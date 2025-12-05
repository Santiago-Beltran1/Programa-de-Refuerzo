import random
import string

def santiagoGenCont(santiagoLong=8, santiagoIncMay=True, santiagoIncNums=True, santiagoIncSimbs=False):
    """Genera una contraseña aleatoria con las características especificadas"""
    santiagoCaracteres = string.ascii_lowercase  # letras minúsculas

    if santiagoIncMay:
        santiagoCaracteres += string.ascii_uppercase  # agregar mayúsculas
    if santiagoIncNums:
        santiagoCaracteres += string.digits  # agregar números 0-9
    if santiagoIncSimbs:
        santiagoCaracteres += "!@#$%&*"  # agregar algunos símbolos

    # Generar la contraseña
    santiagoContra = ""
    for i in range(santiagoLong):
        santiagoAleatorio = random.choice(santiagoCaracteres)
        santiagoContra += santiagoAleatorio

    return santiagoContra


def santiagoEvaluar(santiagoCon):
    """Evalúa qué tan fuerte es una contraseña"""
    santiagoPoints = 0
    santiagoComents = []

    # Longitud
    if len(santiagoCon) >= 8:
        santiagoPoints += 2
        santiagoComents.append("✓ Longitud adecuada")
    else:
        santiagoComents.append("✗ Muy corta (mínimo 8 caracteres)")

    # Mayúsculas
    if any(c.isupper() for c in santiagoCon):
        santiagoPoints += 1
        santiagoComents.append("✓ Contiene mayúsculas")
    else:
        santiagoComents.append("✗ Sin mayúsculas")

    # Números
    if any(c.isdigit() for c in santiagoCon):
        santiagoPoints += 1
        santiagoComents.append("✓ Contiene números")
    else:
        santiagoComents.append("✗ Sin números")

    # Evaluar fortaleza
    if santiagoPoints >= 4:
        fortaleza = "Muy fuerte"
    elif santiagoPoints >= 3:
        fortaleza = "Fuerte"
    elif santiagoPoints >= 2:
        fortaleza = "Moderada"
    else:
        fortaleza = "Débil"

    return fortaleza, santiagoComents


# Probando el generador
print("GENERADOR DE CONTRASEÑAS")
print("=" * 40)

# Generar diferentes tipos de contraseñas
santiago1 = santiagoGenCont(12, True, True, False)
santiago2 = santiagoGenCont(8, True, True, True)
santiago3 = santiagoGenCont(6, False, False, False)

santiagoCons = [
    ("Estándar (12 caracteres)", santiago1),
    ("Con símbolos (8 caracteres)", santiago2),
    ("Solo minúsculas (6 caracteres)", santiago3)
]

for santiagoDesc, contraseña in santiagoCons:
    fortaleza, comentarios = santiagoEvaluar(contraseña)
    print(f"\n{santiagoDesc}:")
    print(f"Contraseña: {contraseña}")
    print(f"Fortaleza: {fortaleza}")
    for comentario in comentarios:
        print(f" {comentario}")
