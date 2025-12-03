import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoAdiv(self, SantiagoMin, SantiagoMax):
        SantiagoN = random.randint(SantiagoMin, SantiagoMax)
        SantiagoInt = 0
        SantiagoAdivinado = False

        while not SantiagoAdivinado:
            SantiagoInt += 1
            SantiagoUser = int(input(f"Adivina el número entre {SantiagoMin} y {SantiagoMax}: "))
            if SantiagoUser == SantiagoN:
                print(f"¡Correcto! Número: {SantiagoN} en {SantiagoInt} intentos")
                SantiagoAdivinado = True
            elif SantiagoUser < SantiagoN:
                print("Muy bajo")
            else:
                print("Muy alto")

Santiago1 = SantiagoB("Juego Adivinar")
Santiago1.SantiagoAdiv(1, 10)  
