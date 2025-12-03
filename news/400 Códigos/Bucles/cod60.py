SantiagoBEst = int(input("Ingrese el número de estudiantes: "))
for SantiagoI in range(SantiagoBEst):
    SantiagoNom = input(f"Nombre del estudiante {SantiagoI+1}: ")
    SantiagoSum = 0
    for SantiagoJ in range(3):
        SantiagoNota = float(input(f"Nota {SantiagoJ+1} de {SantiagoNom}: "))
        SantiagoSum += SantiagoNota
    SantiagoPromedio = SantiagoSum / 3
    print(f"{SantiagoNom} tiene un promedio de {SantiagoPromedio:.2f}")
