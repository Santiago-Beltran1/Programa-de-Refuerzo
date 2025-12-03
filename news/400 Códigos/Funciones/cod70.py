def SantiagoBVelocidad(SantiagoBDistancia, SantiagoBTiempo):
    return SantiagoBDistancia / SantiagoBTiempo

SantiagoBDistancia = float(input("Distancia (km): "))
SantiagoBTiempo = float(input("Tiempo (h): "))
print(f"Velocidad promedio: {SantiagoBVelocidad(SantiagoBDistancia, SantiagoBTiempo):.2f} km/h")
