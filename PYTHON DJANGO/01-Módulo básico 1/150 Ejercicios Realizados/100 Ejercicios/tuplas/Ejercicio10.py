# Sistema de asistencia con tupla

santiagoAsis = (("Carlos", True), ("María", False), ("Pedro", True))

print("Asistencia de estudiantes:")
for santiagoEst, santiagoAsistio in santiagoAsis:
    santiagoEstado = "Asistió" if santiagoAsistio else "No asistió"
    print(f"{santiagoEst}: {santiagoEstado}")
