import random

def SantiagoBAtacar(SantiagoBAtaque, SantiagoBDefensa):
    SantiagoBDano = max(0, SantiagoBAtaque - SantiagoBDefensa + random.randint(-2, 2))
    return SantiagoBDano

def SantiagoBBatalla():
    SantiagoBSalud1 = 30
    SantiagoBSalud2 = 30
    while SantiagoBSalud1 > 0 and SantiagoBSalud2 > 0:
        input("\nPresiona ENTER para atacar")
        SantiagoBDano1 = SantiagoBAtacar(random.randint(4, 10), random.randint(2, 8))
        SantiagoBDano2 = SantiagoBAtacar(random.randint(4, 10), random.randint(2, 8))
        SantiagoBSalud1 -= SantiagoBDano2
        SantiagoBSalud2 -= SantiagoBDano1
        print(f"Jugador 1 golpea con {SantiagoBDano1}, Jugador 2 queda con {SantiagoBSalud2}")
        print(f"Jugador 2 golpea con {SantiagoBDano2}, Jugador 1 queda con {SantiagoBSalud1}")
    print("\n", "Jugador 1 gana" if SantiagoBSalud1 > SantiagoBSalud2 else "Jugador 2 gana")

SantiagoBBatalla()
