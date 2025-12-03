#Indicador de temperatura máxima y mínima en una lista de un rango máximo de 5 temperaturas

santiagoTemps = []

for santiagoI in range(5):
    santiagoT = float(input(f"Temperatura {santiagoI+1}: "))
    santiagoTemps.append(santiagoT)

print("Temperaturas:", santiagoTemps)
print("Máxima:", max(santiagoTemps))
print("Mínima:", min(santiagoTemps))
