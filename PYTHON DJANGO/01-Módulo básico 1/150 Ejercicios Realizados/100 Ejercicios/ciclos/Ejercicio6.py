#Indicador de tipo de metraje según la duración del mismo

santiagoDuracion = int(input("Duración de la película en minutos: "))
if santiagoDuracion < 40:
    santiagoCat = "Cortometraje"
elif 40 <= santiagoDuracion <= 90:
    santiagoCat = "Película media"
else:
    santiagoCat = "Película larga"
print("La película es de tipo:", santiagoCat)
