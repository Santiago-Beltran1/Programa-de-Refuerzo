#Sistema de tomar asistencia

santiagoEsts = int(input("¿Cuántos estudiantes?: "))

for santiagoI in range(santiagoEsts):
    santiagoNom = input("Nombre del estudiante: ")
    santiagoAsis = input("¿Asistió? (si/no): ")

    if santiagoAsis.lower() == "si":
        print(f"{santiagoNom}: Presente")
    else:
        santiagoRazon = input("Motivo de inasistencia: ")
        print(f"{santiagoNom}: Ausente ({santiagoRazon})")
