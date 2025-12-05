import math
from itertools import permutations

def santiagoCalcDis(santiagoCiudad1, santiagoCiudad2):
    """
    Calcula la distancia euclidiana entre dos ciudades
    Cada ciudad tiene coordenadas (x, y)
    """
    santiagoX1, santiagoy1 = santiagoCiudad1
    santiagoX2, santiagoy2 = santiagoCiudad2
    distancia = math.sqrt((santiagoX2 - santiagoX1)**2 + (santiagoy2 - santiagoy1)**2)
    return round(distancia, 2)

def santiagoCalcDisTotal(santiagoCiudades, santiagoRuta):
    """
    Calcula la distancia total de una ruta completa
    La ruta es una lista de índices de ciudades
    """
    santiagoDisTotal = 0
    for i in range(len(santiagoRuta)):
        ciudad_actual = santiagoCiudades[santiagoRuta[i]]
        siguiente_ciudad = santiagoCiudades[santiagoRuta[(i + 1) % len(santiagoRuta)]]  # Para cerrar el ciclo
        distancia = santiagoCalcDis(ciudad_actual, siguiente_ciudad)
        santiagoDisTotal += distancia
    return round(santiagoDisTotal, 2)

def santiagoMetodFuerzaBruta(ciudades):
    """
    Encuentra la ruta óptima probando todas las combinaciones posibles
    ¡ADVERTENCIA: Solo usar con pocas ciudades por complejidad computacional!
    """
    num_ciudades = len(ciudades)
    print(f"Iniciando búsqueda exhaustiva para {num_ciudades} ciudades...")
    mejor_distancia = float('inf')
    mejor_ruta = None
    for ruta in permutations(range(num_ciudades)):
        distancia = santiagoCalcDisTotal(ciudades, ruta)
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

    ruta_optima, distancia_optima = santiagoMetodFuerzaBruta(ciudades)
    print("\nResultado final:")
    print(f"Ruta óptima: {ruta_optima}")
    print(f"Distancia total de la ruta óptima: {distancia_optima}")
