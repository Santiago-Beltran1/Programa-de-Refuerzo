#Contador de letras "a" en una frase

santiagoFrase = input("Ingrese una frase: ")
santiagoCont = 0
for santiagoL in santiagoFrase:
    if santiagoL.lower() == "a":
        santiagoCont += 1
print("Cantidad de letras 'a':", santiagoCont)
