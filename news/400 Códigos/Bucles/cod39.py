SantiagoBN = 41
SantiagoPrimo = True
for SantiagoB in range(2, int(SantiagoBN ** 0.5) + 1):
    if SantiagoBN % SantiagoB == 0:
        SantiagoPrimo = False
        break
print(f"El número {SantiagoBN} es primo:", SantiagoPrimo)
