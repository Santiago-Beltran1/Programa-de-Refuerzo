import random

def SantiagoBJuegoPPT():
    SantiagoOpc = ["piedra", "papel", "tijera"]
    SantiagoJug = input("Elige piedra, papel o tijera: ").lower()
    SantiagoCPU = random.choice(SantiagoOpc)
    print(f"La máquina eligió: {SantiagoCPU}")

    if SantiagoJug == SantiagoCPU:
        print("Empate.")
    elif (SantiagoJug == "piedra" and SantiagoCPU == "tijera") or \
         (SantiagoJug == "papel" and SantiagoCPU == "piedra") or \
         (SantiagoJug == "tijera" and SantiagoCPU == "papel"):
        print("Ganaste ")
    else:
        print("Perdiste ")

SantiagoBJuegoPPT()
