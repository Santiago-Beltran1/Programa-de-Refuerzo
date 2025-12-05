import random
import time

def santiagoCrearT(santiagoFilas, santiagoColumnas, santiagoDensidad=0.3):
    """
    Crea un tablero inicial con células vivas y muertas.
    densidad: probabilidad de que una célula esté viva inicialmente.
    """
    santiagoTablero = []
    for i in range(santiagoFilas):
        santiagoFila = []
        for j in range(santiagoColumnas):
            santiagoEstaViva = 1 if random.random() < santiagoDensidad else 0
            santiagoFila.append(santiagoEstaViva)
        santiagoTablero.append(santiagoFila)
    return santiagoTablero

def santiagoContarVecinosVivos(santiagoTablero, santiagoFila, santiagoColumna):
    """
    Cuenta cuántos vecinos vivos tiene una célula.
    Considera las 8 células adyacentes (incluidas las diagonales).
    """
    santiagoFilas = len(santiagoTablero)
    santiagoColumnas = len(santiagoTablero[0])
    santiagoVecinosVivos = 0
    santiagoDirec = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for df, dc in santiagoDirec:
        nueva_fila = santiagoFila + df
        nueva_columna = santiagoColumna + dc
        if 0 <= nueva_fila < santiagoFilas and 0 <= nueva_columna < santiagoColumnas:
            santiagoVecinosVivos += santiagoTablero[nueva_fila][nueva_columna]
    return santiagoVecinosVivos

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
            vecinos = santiagoContarVecinosVivos(tablero, i, j)
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

def santiagoMosTab(santiagoTablero, santiagoGeneración):
    """Muestra el tablero en formato visual."""
    print(f"\nGeneración {santiagoGeneración}:")
    for santiagoFila in santiagoTablero:
        santiagoLinea = ""
        for santiagoCelula in santiagoFila:
            santiagoLinea += "■ " if santiagoCelula == 1 else ". "
        print(santiagoLinea)

if __name__ == "__main__":
    filas, columnas = 10, 20
    tablero = santiagoCrearT(filas, columnas, santiagoDensidad=0.3)

    santiagoGeneraciones = 5
    for gen in range(1, santiagoGeneraciones + 1):
        santiagoMosTab(tablero, gen)
        tablero = aplicar_reglas(tablero)
        time.sleep(1)  # Pausa para que puedas ver cada generación
