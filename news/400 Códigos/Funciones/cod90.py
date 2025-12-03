import random

def SantiagoBPreguntas():
    SantiagoPreg = [
        ("¿Cuál es el planeta más grande del sistema solar?", "jupiter"),
        ("¿Quién pintó la Mona Lisa?", "leonardo da vinci"),
        ("¿En qué continente está Egipto?", "africa"),
        ("¿Cuántos huesos tiene el cuerpo humano adulto?", "206")
    ]
    SantiagoP = random.choice(SantiagoPreg)
    SantiagoR = input(SantiagoP[0] + " ").lower()
    if SantiagoR == SantiagoP[1]:
        print("¡Correcto!")
    else:
        print("Incorrecto, la respuesta era:", SantiagoP[1])

SantiagoBPreguntas()
