#Reemplazar todas las vocales de un texto por '*'

def santiagoReemV(texto):
    santiagoVocales = "aeiouAEIOU"
    santiagoNewText = ""
    for santiagoLetra in texto:
        if santiagoLetra in santiagoVocales:
            santiagoNewText += "*"
        else:
            santiagoNewText += santiagoLetra
    return santiagoNewText

print(santiagoReemV("Me gusta la salchipapa"))  
