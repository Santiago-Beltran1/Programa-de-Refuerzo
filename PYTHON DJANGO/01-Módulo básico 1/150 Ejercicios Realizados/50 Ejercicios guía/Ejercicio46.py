#Contar letras mayúsculas y minúsculas en un texto

def santiagoContar(santiagoText):
    santiagoMayus = 0
    santiagoMinus = 0
    for santiagoC in santiagoText:
        if santiagoC.isupper():
            santiagoMayus += 1
        elif santiagoC.islower():
            santiagoMinus += 1
    return print("Hay", santiagoMayus, "letras mayúsculas y", santiagoMinus, "minúsculas")

print(santiagoContar("Servicio Nacional de Aprendizaje"))