print("Tabla del 1 al 5 que se repite justamente de 5 en 5 cada fila:")
print("-" * 40)
for SantiagoI in range(1, 100):
    for SantiagoJ in range(1, 6):
        print(f"{SantiagoI * SantiagoJ:4}", end="")
    print()  # Salto de línea para nueva fila
