#Contador y almacenador de palabras en un texto

santiagoFrase = input("Escribe una frase: ")
santiagoPals = santiagoFrase.lower().split() 

santiagoUnics = list(set(santiagoPals))  
for santiagoP in santiagoUnics:
    print(f"La palabra '{santiagoP}' aparece {santiagoPals.count(santiagoP)} veces")
