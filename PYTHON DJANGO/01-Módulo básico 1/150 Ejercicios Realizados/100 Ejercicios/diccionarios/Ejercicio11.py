#Almacenador de cuántas veces aparece una palabra en una frase

santiagoText = input("Escribe un texto: ")
santiagoPals = santiagoText.split()
santiagoCount = {}

for santiagoP in santiagoPals:
    santiagoCount[santiagoP] = santiagoCount.get(santiagoP, 0) + 1

print("Frecuencia de palabras:", santiagoCount)
