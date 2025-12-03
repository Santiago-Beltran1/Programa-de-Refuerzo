#Promedio de notas de estudiantes

santiagoCal = {"Juan": [3.5, 4.0, 4.5], "Ana": [4.2, 3.9, 4.8], "Pedro": [2.5, 3.0, 3.7]}

for santiagoAl, santiagoNotas in santiagoCal.items():
    santiagoProm = sum(santiagoNotas) / len(santiagoNotas)
    print(f"{santiagoAl} tiene un promedio de {santiagoProm:.2f}")
