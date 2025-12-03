SantiagoB = {"Paquete de arroz": 5, "Gaseosas": 2, "Cepillos": 0}

for SantiagoProd, SantiagoCant in SantiagoB.items():
    if SantiagoCant <= 3:
        print(f"{SantiagoProd} está bajo en stock.")
        SantiagoB[SantiagoProd] += 15

print(f"Stock actualizado con reposición: {SantiagoB}")
