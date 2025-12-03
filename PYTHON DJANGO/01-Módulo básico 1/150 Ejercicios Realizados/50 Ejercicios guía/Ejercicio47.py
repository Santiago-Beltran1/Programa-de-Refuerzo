#Invertir palabras de una frase sin cambiar el orden
def santiagoInvertir(santiagoFrase):
    santiagoPalabras = santiagoFrase.split()
    santiagoInverts = []
    for santiagoP in santiagoPalabras:
        santiagoInverts.append(santiagoP[::-1])
    return " ".join(santiagoInverts)

print(santiagoInvertir("El SENA es donde yo estudio"))  
