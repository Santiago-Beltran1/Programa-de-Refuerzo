import random
import time

def crear_tablero(filas, columnas, densidad=0.3):
    """
    Crea un tablero inicial con células vivas y muertas.
    densidad: probabilidad de que una célula esté viva inicialmente.
    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero

def contar_vecinos_vivos(tablero, fila, columna):
    """
    Cuenta cuántos vecinos vivos tiene una célula.
    Considera las 8 células adyacentes (incluidas las diagonales).
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos

def aplicar_reglas(tablero):
    """
    Aplica las reglas del Juego de la Vida para generar la siguiente generación.
    Reglas:
    1. Célula viva con < 2 vecinos vivos: muere (soledad).
    2. Célula viva con 2-3 vecinos vivos: sobrevive.
    3. Célula viva con > 3 vecinos vivos: muere (sobrepoblación).
    4. Célula muerta con exactamente 3 vecinos vivos: nace.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]
            if celula_actual == 1:
                if vecinos < 2 or vecinos > 3:
                    nuevo_tablero[i][j] = 0  # Muere
                else:
                    nuevo_tablero[i][j] = 1  # Sobrevive
            else:
                if vecinos == 3:
                    nuevo_tablero[i][j] = 1  # Nace
    return nuevo_tablero

def mostrar_tablero(tablero, generacion):
    """Muestra el tablero en formato visual."""
    print(f"\nGeneración {generacion}:")
    for fila in tablero:
        linea = ""
        for celula in fila:
            linea += "■ " if celula == 1 else ". "
        print(linea)

if __name__ == "__main__":
    filas, columnas = 10, 20
    tablero = crear_tablero(filas, columnas, densidad=0.3)

    generaciones = 5
    for gen in range(1, generaciones + 1):
        mostrar_tablero(tablero, gen)
        tablero = aplicar_reglas(tablero)
        time.sleep(1)  # Pausa para que puedas ver cada generación
