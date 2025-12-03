#Mostrar cuadrados y cubos de números aleatorios

import random

santiagoNums = [random.randint(1, 10) for _ in range(10)]

for santiagoN in santiagoNums:
    print(f"Número: {santiagoN}, Cuadrado: {santiagoN**2}, Cubo: {santiagoN**3}")
