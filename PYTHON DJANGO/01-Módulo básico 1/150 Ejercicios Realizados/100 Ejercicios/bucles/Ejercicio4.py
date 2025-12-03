#Juego de adivinanza en el cual si no se adivina la palabra en 3 intentos el usuario pierde

santiagoP = "Santiago"
for santiagoI in range(3):
    santiagoInten = input("Adivine la palabra secreta: ")
    if santiagoInten == santiagoP:
        print("¡Correcto!")
        break
else:
    print("Se acabaron los intentos")
