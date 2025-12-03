def SantiagoBNumerosPares(SantiagoBLimite):
    for SantiagoBNum in range(2, SantiagoBLimite + 1, 2):
        print(SantiagoBNum)

SantiagoBLimite = int(input("Límite superior: "))
SantiagoBNumerosPares(SantiagoBLimite)
