def SantiagoBEnvio(SantiagoPeso):
    if SantiagoPeso <= 1:
        return 5000
    elif SantiagoPeso <= 5:
        return 10000
    else:
        return 20000

peso = float(input("Peso del paquete (kg): "))
print(f"Costo de envío: ${SantiagoBEnvio(peso)}")
