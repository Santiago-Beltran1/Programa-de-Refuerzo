import random

def SantiagoBLaberinto(SantiagoBFilas, SantiagoBColumnas):
    for _ in range(SantiagoBFilas):
        print("".join(random.choice(["⬜", "⬛"]) for _ in range(SantiagoBColumnas)))

SantiagoBLaberinto(10, 20)
