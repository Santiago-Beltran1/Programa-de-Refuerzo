import numpy as SantiagoNp

def SantiagoTablero(SantiagoFilas, SantiagoColumnas):
    return SantiagoNp.indices((SantiagoFilas, SantiagoColumnas)).sum(axis=0) % 2

print(f"Tablero de Ajedrez 0 cuadros blancos 1 cuadros negros: \n {SantiagoTablero(8,8)}")
