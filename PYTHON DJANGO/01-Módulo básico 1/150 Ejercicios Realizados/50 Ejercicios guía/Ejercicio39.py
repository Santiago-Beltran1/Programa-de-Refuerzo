#EJERCICIOS FINALES - Juego de aventura de texto

def santiagoAven():
    print("Estás en una cueva oscura. ¿Izquierda o derecha?")
    santiagoElec = input("> ").lower()

    if santiagoElec == "izquierda":
        print("Te encuentras un dragón. ¿Luchar o correr?")
        santiagoAccion = input("> ").lower()
        if santiagoAccion == "luchar":
            print("Ganaste. ¡Eres un héroe!")
        else:
            print("Escapaste pero te perdiste en la cueva. Fin.")
    elif santiagoElec == "derecha":
        print("Caíste en un pozo. Fin.")
    else:
        print("No entendí tu elección. Fin.")

santiagoAven()
