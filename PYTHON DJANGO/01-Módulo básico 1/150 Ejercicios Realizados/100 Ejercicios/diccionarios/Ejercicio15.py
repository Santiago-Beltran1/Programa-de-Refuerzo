#Simulador de sistema de asistencias con diccionario

santiagoAsis = {}
santiagoN = int(input("¿Cuántos estudiantes? "))

for santiagoI in range(santiagoN):
    santiagoNom = input(f"Nombre del estudiante {santiagoI+1}: ")
    santiagoPres = input("¿Presente? (si/no): ").lower() == "si"
    santiagoAsis[santiagoNom] = santiagoPres

print("Asistencia final:", santiagoAsis)
