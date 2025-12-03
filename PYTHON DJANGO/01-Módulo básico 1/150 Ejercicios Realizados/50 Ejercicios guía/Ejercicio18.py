# Calculadora de calificaciones
santiagoCal = [3.0, 2.2, 3.7, 4.5, 3.9, 4.4, 4.1, 1.5]

print("Calificaciones del estudiante: ")
print(santiagoCal)

# Estadísticas básicas
santiagoTotal = len(santiagoCal)
santiagoSumNotas = sum(santiagoCal) 
santiagoProm = santiagoSumNotas / santiagoTotal
santiagoMayor = max(santiagoCal) 
santiagoMenor = min(santiagoCal) 

print(f"\n--- ESTADÍSTICAS ---")
print(f"Total de materias: {santiagoTotal}")
print(f"Suma de todas las notas: {santiagoSumNotas}")
print(f"Promedio: {santiagoProm:.2f}") 
print(f"Nota más alta: {santiagoMayor}")
print(f"Nota más baja: {santiagoMenor}")


santiagoAP = 0
for santiagon in santiagoCal: 
    if santiagon >= 3.0:
        santiagoAP = santiagoAP + 1
print(f"Usted aprobo {santiagoAP} de {santiagoTotal} materias")