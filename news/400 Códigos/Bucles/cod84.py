SantiagoA = 0
SantiagoR = 0

for SantiagoEst in range(10):
    SantiagoNota = float(input("Ingrese la nota del estudiante: "))
    if SantiagoNota >= 3.0:
        SantiagoA += 1
    else:
        SantiagoR += 1

print("Estudiantes que han aprobado: {SantiagoA}")
print("Estudiantes que han reprobado: {SantiagoR}")
