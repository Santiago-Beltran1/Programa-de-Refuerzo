#Calcular IMC

santiagoPeso = float(input("Peso (kg): "))
santiagoAlt = float(input("Altura (m): "))
santiagoIMC = santiagoPeso / (santiagoAlt**2)
if santiagoIMC < 18.5:
    print("Bajo peso")
elif santiagoIMC < 25:
    print("Normal")
elif santiagoIMC < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
