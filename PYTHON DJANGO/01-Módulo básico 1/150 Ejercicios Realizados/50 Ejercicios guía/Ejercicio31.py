import random

class santiagoAnimal:
    def __init__(self, santiagoNom, santiagoTip, santiagoEnergy=100, santiagoPosX=0, santiagoPosY=0):
        self.nombre = santiagoNom
        self.tipo = santiagoTip  # "herbívoro", "carnívoro"
        self.energia = santiagoEnergy
        self.posicion_x = santiagoPosX
        self.posicion_y = santiagoPosY
        self.santiagoVivo = True

    def santiagoMov(self):
        """Mueve el animal aleatoriamente"""
        if self.santiagoVivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5  # Moverse cuesta energía

            print(f"{self.nombre} se movió a ({self.posicion_x}, {self.posicion_y}). Energía: {self.energia}")

            if self.energia <= 0:
                self.santiagoVivo = False
                print(f"{self.nombre} ha muerto por falta de energía.")


# Prueba del código
santiagoA1 = santiagoAnimal("Leo", "carnívoro")

for _ in range(25):
    santiagoA1.santiagoMov()
    if not santiagoA1.santiagoVivo:
        break
