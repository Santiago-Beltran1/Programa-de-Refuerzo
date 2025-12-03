SantiagoBN = [3.5, 31.2, 3.8, 5.0, 3.9]
SantiagoSum = 0
for SantiagoB in SantiagoBN:
    SantiagoSum += SantiagoB
SantiagoProm = SantiagoSum / len(SantiagoBN)
print("El promedio de notas es:", round(SantiagoProm, 2))
