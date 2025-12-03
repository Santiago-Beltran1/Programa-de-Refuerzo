SantiagoB = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
SantiagoTemps = []

for SantiagoDia in SantiagoB:
    SantiagoTemp = float(input(f"Temperatura de {SantiagoDia}: "))
    SantiagoTemps.append(SantiagoTemp)

SantiagoProm = sum(SantiagoTemps) / len(SantiagoTemps)
print(f"\nTemperatura promedio semanal: {SantiagoProm}")
print(f"Temperatura más alta: {max(SantiagoTemps)}")
print(f"Temperatura más baja: {min(SantiagoTemps)}")
