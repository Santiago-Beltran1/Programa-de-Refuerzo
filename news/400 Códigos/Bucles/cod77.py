SantiagoBR = {"Bueno": 0, "Regular": 0, "Malo": 0}

for SantiagoI in range(10):
    SantiagoResp = input("¿Cómo califica el servicio? (Bueno/Regular/Malo): ").capitalize()
    if SantiagoResp in SantiagoBR:
        SantiagoBR[SantiagoResp] += 1

print("\nResultados:")
for SantiagoClave, SantiagoValor in SantiagoBR.items():
    print(f"{SantiagoClave}: {SantiagoValor}")
