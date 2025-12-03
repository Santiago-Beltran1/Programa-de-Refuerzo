#Promediador de notas según alumnos de la tupla

santiagoAlumns = ("Laura", "Andrés", "Sofía")
santiagoNots = []

for santiagoAlumn in santiagoAlumns:
    nota = float(input(f"Nota de {santiagoAlumn}: "))
    santiagoNots.append(nota)

for i, santiagoAlumn in enumerate(santiagoAlumns):
    print(f"{santiagoAlumn}: {santiagoNots[i]}")

print("Promedio general:", sum(santiagoNots)/len(santiagoNots))
