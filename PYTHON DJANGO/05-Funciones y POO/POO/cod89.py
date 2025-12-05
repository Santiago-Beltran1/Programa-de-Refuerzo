import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoJug(self, SantiagoU):
        SantiagoOpc = ["piedra", "papel", "tijera"]
        SantiagoPC = random.choice(SantiagoOpc)
        if SantiagoU == SantiagoPC:
            return "Empate", SantiagoPC
        elif (SantiagoU == "piedra" and SantiagoPC == "tijera") or \
             (SantiagoU == "papel" and SantiagoPC == "piedra") or \
             (SantiagoU == "tijera" and SantiagoPC == "papel"):
            return "Ganaste", SantiagoPC
        else:
            return "Perdiste", SantiagoPC

Santiago1 = SantiagoB("Juego")
SantiagoR, SantiagoCpu = Santiago1.SantiagoJug("piedra")
print(f"PC eligió {SantiagoCpu}, Resultado: {SantiagoR}")
