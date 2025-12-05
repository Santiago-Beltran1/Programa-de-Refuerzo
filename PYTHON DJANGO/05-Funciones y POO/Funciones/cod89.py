def SantiagoBPasos():
    SantiagoPasos = int(input("Ingrese cantidad de pasos del día: "))
    SantiagoCalo = SantiagoPasos * 0.04
    SantiagoDist = SantiagoPasos * 0.8 / 1000
    print(f"Distancia: {SantiagoDist:.2f} km")
    print(f"Calorías aproximadas quemadas: {SantiagoCalo:.1f}")

SantiagoBPasos()
