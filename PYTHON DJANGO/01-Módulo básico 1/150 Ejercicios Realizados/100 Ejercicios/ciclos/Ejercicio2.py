#Notificador de temperatura

santiagoDias = int(input("¿Cuántos días desea registrar?: "))

for santiagoI in range(santiagoDias):
    santiagoTemp = float(input(f"Temperatura del día {santiagoI+1}, en grados Celsius: "))

    if santiagoTemp > 35:
        print("Alerta: Temperatura muy alta")
    elif santiagoTemp < 5:
        print("Alerta: Temperatura muy baja")
    else:
        print("Temperatura normal")
