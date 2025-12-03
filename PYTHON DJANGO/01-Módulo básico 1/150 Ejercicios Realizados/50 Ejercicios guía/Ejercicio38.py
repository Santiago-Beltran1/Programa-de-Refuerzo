#EJERCICIOS FINALES - Analizador de datos CSV

import csv
from statistics import mean
import matplotlib.pyplot as plt

def santiagoAnalizarCSV(nombre_archivo):
    santiagoDatos = []
    with open(nombre_archivo, newline='') as archivo:
        santiagoLector = csv.reader(archivo)
        next(santiagoLector)  # Saltar encabezado
        for fila in santiagoLector:
            santiagoDatos.append(float(fila[1]))  # Suponemos que los datos están en la segunda columna

    print("Media:", mean(santiagoDatos))
    plt.hist(santiagoDatos, bins=5)
    plt.title("Histograma de datos")
    plt.show()

# Usa un archivo CSV con al menos dos columnas para probar.
# analizar_csv("datos.csv")
