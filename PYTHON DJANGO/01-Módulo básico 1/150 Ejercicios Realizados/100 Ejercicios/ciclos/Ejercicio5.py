#Simulador de resultado de un partido

santiagoPartidos = int(input("¿Cuántos partidos registrar?: "))
santiagoRivalGol = 1

for santiagoI in range(santiagoPartidos):
    santiagoEquipos = input("Nombre del equipo: ")
    santiagoGoles = int(input("Goles anotados: "))

    if santiagoGoles >= santiagoRivalGol:
        print(f"{santiagoEquipos}: Victoria")
    elif santiagoGoles == santiagoRivalGol:
        print(f"{santiagoEquipos}: Victoria ajustada")
    elif santiagoGoles == santiagoRivalGol:
        print(f"{santiagoEquipos}: Empate")
    else:
        print(f"{santiagoEquipos}: Derrota")
