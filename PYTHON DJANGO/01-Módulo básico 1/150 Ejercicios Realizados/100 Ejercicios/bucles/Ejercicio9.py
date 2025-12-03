#Contador de vocales en una palabra

santiagoP = input("Ingrese una palabra: ")
santiagoC = 0

for santiagoLetra in santiagoP:
    if santiagoLetra.lower() in "aeiou":
        santiagoC += 1
        
print("Cantidad de vocales:", santiagoC)
