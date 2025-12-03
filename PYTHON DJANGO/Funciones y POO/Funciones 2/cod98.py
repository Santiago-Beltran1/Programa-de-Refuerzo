import random as SantiagoRandom

def SantiagoSims(SantiagoCiu):
    SantiagoEstados = ["Soleado","Nublado","Lluvioso","Tormenta","Nevado"]
    for ciudad in SantiagoCiu:
        SantiagoClima = SantiagoRandom.choice(SantiagoEstados)
        SantiagoTemp = SantiagoRandom.randint(-5,35)
        print(f"Clima en {ciudad}: {SantiagoClima} con {SantiagoTemp}°C")

SantiagoSims(["Mosquera","Funza","Madrid"])
