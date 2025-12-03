# Juego de adivinar colores con varios intentos

santiagoColSec = "azul"
santiagoMax = 3
santiagoAct = 1

print("¡Bienvenido al juego de adivinanza!")
print("Tienes", santiagoMax, "intentos para adivinar el color secreto")

while santiagoAct <= santiagoMax:
    print("\n--- Intento", santiagoAct, "de", santiagoMax, "---")
    

    if santiagoAct == 1:
        adivinanza = str(input("Ingrese un color: "))
    elif santiagoAct == 2:
        adivinanza = str(input("Ingrese un color: "))
    else:
        adivinanza = str(input("Ingrese un color: "))

    print("Tu adivinanza:", adivinanza)

    if adivinanza == santiagoColSec:
        print("¡GANASTE! El color era", santiagoColSec)
        break  
    elif adivinanza != santiagoColSec:
        print("Color incorrecto, intenta otra vez")

    santiagoAct += 1  

    if santiagoAct > santiagoMax:
        print("\n¡Se acabaron los intentos! El color era", santiagoColSec)
