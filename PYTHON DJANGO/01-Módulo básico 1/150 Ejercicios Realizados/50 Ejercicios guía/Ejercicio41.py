#Contador de vocales que hay en una frase

santiagoFrase = input("Ingresa una frase: ").lower()
santiagoVoc = "aeiou"
santiagoC = 0
for santiagoL in santiagoFrase:
    if santiagoL in santiagoVoc:
        santiagoC += 1
print("Número de vocales:", santiagoC)
