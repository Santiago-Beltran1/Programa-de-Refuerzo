def SantiagoSemaforo(SantiagoColor):
    if SantiagoColor.lower() == "rojo":
        return "Detente"
    elif SantiagoColor.lower() == "amarillo":
        return "Precaución"
    elif SantiagoColor.lower() == "verde":
        return "Avanza"
    else:
        return "Color inválido"

def SantiagoControlSemaforo():
    SantiagoColor = input("Color del semáforo: ")
    print(SantiagoSemaforo(SantiagoColor))

SantiagoControlSemaforo()
