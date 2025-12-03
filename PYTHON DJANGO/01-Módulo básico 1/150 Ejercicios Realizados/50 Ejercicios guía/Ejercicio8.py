# Clasificador de notas
santiagoNota = float(input("ingrese su calificación: "))
if santiagoNota >= 4.5:
    santiagoCal = "Excelente"
    santiagoMSG = "Aprobada"
elif santiagoNota >= 3.0: 
    santiagoCal = "Buena"
    santiagoMSG = "Aprobada, buen trabajo, puede mejorar"
else:
    santiagoCal = "Necesita mejorar"
    santiagoMSG = "Desaprobado, estudia más para la próxima"
    
print("Tu nota es:", santiagoNota)
print("Calificación:", santiagoCal)
print("Materia:", santiagoMSG)