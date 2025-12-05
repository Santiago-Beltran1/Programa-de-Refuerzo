def SantiagoBProductividad():
    SantiagoBTareas = int(input("Tareas completadas: "))
    SantiagoBErrores = int(input("Errores cometidos: "))
    SantiagoBHoras = int(input("Horas trabajadas: "))

    SantiagoBPuntaje = (SantiagoBTareas * 10) - (SantiagoBErrores * 5) + (SantiagoBHoras * 2)
    print(f"Puntaje de productividad: {SantiagoBPuntaje}")

SantiagoBProductividad()
