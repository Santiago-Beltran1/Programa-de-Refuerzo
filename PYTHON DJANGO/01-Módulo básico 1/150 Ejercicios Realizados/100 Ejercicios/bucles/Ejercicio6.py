#Juego de piedra, papel y tijeras - Simulación

import random
santiagoOP = ["piedra", "papel", "tijera"]

while True:
    santiagoGamer = input("Elija piedra, papel o tijera (o 'salir'): ")
    if santiagoGamer == "salir":
        break
    
    santiagoCompu = random.choice(santiagoOP)
    print("Computadora eligió:", santiagoCompu)
    if santiagoGamer == santiagoCompu:
        print("Empate")
    elif (santiagoGamer == "piedra" and santiagoCompu == "tijera") or (santiagoGamer == "papel" and santiagoCompu == "piedra") or (santiagoGamer == "tijera" and santiagoCompu == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste")
