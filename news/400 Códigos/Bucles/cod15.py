print("Forma tradicional: ")
SantiagoB_Par = []
for SantiagoX in range(35):
    if SantiagoX % 2 == 0:
        SantiagoB_Par.append(SantiagoX)
print(SantiagoB_Par)

print("Por comprensión: ")
SantiagoPar = [SantiagoX for SantiagoX in range(40) if SantiagoX % 2 == 0]
print(SantiagoPar)