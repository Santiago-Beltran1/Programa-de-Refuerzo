import math
from itertools import permutations

def calcular_distancia(ciudad1, ciudad2):
    """
    Calcula la distancia euclidiana entre dos ciudades
    Cada ciudad tiene coordenadas (x, y)
    """
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)

def calcular_distancia_total_ruta(ciudades, ruta):
    """
    Calcula la distancia total de una ruta completa
    La ruta es una lista de índices de ciudades
    """
    distancia_total = 0
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]]  # Para cerrar el ciclo
        distancia = calcular_distancia(ciudad_actual, siguiente_ciudad)
        distancia_total += distancia
    return round(distancia_total, 2)

def metodo_fuerza_bruta(ciudades):
    """
    Encuentra la ruta óptima probando todas las combinaciones posibles
    ¡ADVERTENCIA: Solo usar con pocas ciudades por complejidad computacional!
    """
    num_ciudades = len(ciudades)
    print(f"Iniciando búsqueda exhaustiva para {num_ciudades} ciudades...")
    mejor_distancia = float('inf')
    mejor_ruta = None
    for ruta in permutations(range(num_ciudades)):
        distancia = calcular_distancia_total_ruta(ciudades, ruta)
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_ruta = ruta
    print(f"Mejor ruta encontrada: {mejor_ruta} con distancia total: {mejor_distancia}")
    return mejor_ruta, mejor_distancia

if __name__ == "__main__":
    # Definimos algunas ciudades (x, y)
    ciudades = [
        (0, 0),
        (1, 5),
        (5, 2),
        (6, 6)
    ]

    ruta_optima, distancia_optima = metodo_fuerza_bruta(ciudades)
    print("\nResultado final:")
    print(f"Ruta óptima: {ruta_optima}")
    print(f"Distancia total de la ruta óptima: {distancia_optima}")
