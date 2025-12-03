SantiagoN = 4
SantiagoR = 1

print("Paso a paso para llegar al factorial de 3")
for SantiagoB in range(1, SantiagoN + 1):
    SantiagoR *= SantiagoB
    print(f"Paso {SantiagoB}: {SantiagoR}")
print(f"El factorial del número 4 es {SantiagoR}:")
