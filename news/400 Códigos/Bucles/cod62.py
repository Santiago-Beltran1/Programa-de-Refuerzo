SantiagoBMeS = ["Enero", "Febrero", "Marzo", "Abril"]
SantiagoVent = []

for SantiagoMes in SantiagoBMeS:
    SantiagoValor = float(input(f"Ingrese ventas de {SantiagoMes}: "))
    SantiagoVent.append(SantiagoValor)

SantiagoProm = sum(SantiagoVent) / len(SantiagoVent)
print(f"El promedio mensual de las ventas es de: {SantiagoProm}")
