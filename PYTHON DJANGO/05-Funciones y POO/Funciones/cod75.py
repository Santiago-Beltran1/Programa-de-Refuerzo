import random

def SantiagoBClima():
    SantiagoBTemperatura = random.randint(10, 35)
    SantiagoBCondicion = random.choice(["Soleado", "Nublado", "Lluvioso", "Ventoso"])
    print(f"Temperatura: {SantiagoBTemperatura}°C, Clima: {SantiagoBCondicion}")

SantiagoBClima()
