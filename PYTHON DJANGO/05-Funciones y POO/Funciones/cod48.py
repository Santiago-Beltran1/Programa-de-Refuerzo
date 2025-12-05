import random

def SantiagoJuego():
    SantiagoNum = random.randint(1, 10)
    print("Adivina el número entre 1 y 10")
    while True:
        try:
            SantiagoIntento = int(input("Tu intento: "))
            if SantiagoIntento == SantiagoNum:
                print("¡Correcto!")
                break
            else:
                print("Incorrecto, intenta otra vez.")
        except:
            print("Ingresa un número válido.")

SantiagoJuego()
