#Conversor de medidas

santiagoUnids = ("metros", "centímetros", "milímetros")

santiagoValor = float(input("Ingresa el valor en metros: "))

print(f"{santiagoValor} metros = {santiagoValor*100} {santiagoUnids[1]}")
print(f"{santiagoValor} metros = {santiagoValor*1000} {santiagoUnids[2]}")
