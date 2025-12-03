SantiagoBCap = float(input("Ingrese el capital inicial: "))
SantiagoTasa = float(input("Ingrese la tasa de interés (%): ")) / 100
SantiagoMes = int(input("Ingrese el número de meses: "))

SantiagoInt = SantiagoBCap * SantiagoTasa * SantiagoMes
SantiagoTot = SantiagoBCap + SantiagoInt

print(f"Interés ganado: {SantiagoInt}")
print(f"Total acumulado: {SantiagoTot}")
