#Imprimir materias e instructor que las dictara

santiagoCursos = {"Matemáticas": "Ins. López", "SST": "Ins. Juan", "Inglés": "Ins. Laura"}

print("Cursos y sus instructores:")
for santiagoCurso, santiagoProf in santiagoCursos.items():
    print(f"{santiagoCurso} es dictado por {santiagoProf}")
