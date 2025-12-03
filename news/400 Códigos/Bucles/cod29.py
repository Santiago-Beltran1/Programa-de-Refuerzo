import csv

with open('santiago.csv', 'r', newline='', encoding='utf-8') as SantiagoArch:
    SantiagoLector = csv.reader(SantiagoArch)
    next(SantiagoLector)  # Saltar la cabecera
    SantiagoTotal = 0
    for SantiagoFila in SantiagoLector:
        SantiagoValor = float(SantiagoFila[2])  # Asumiendo que la columna 2 contiene ventas
        SantiagoTotal += SantiagoValor

print(f"Total de ventas: {SantiagoTotal}")
