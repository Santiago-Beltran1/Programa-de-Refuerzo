#EJERCICIOS FINALES - Calculadora Científica

import math

def santiagoCalcScience():
    print("Calculadora Científica Básica")
    print("1. Potencia")
    print("2. Raíz cuadrada")
    print("3. Factorial")
    santiagoOP = input("Elige una opción: ")

    if santiagoOP == "1":
        santiagoBase = float(input("Base: "))
        santiagoExponente = float(input("Exponente: "))
        print("Resultado:", santiagoBase ** santiagoExponente)
    elif santiagoOP == "2":
        santiagoNum = float(input("Número para raíz cuadrada: "))
        print("Resultado:", math.sqrt(santiagoNum))
    elif santiagoOP == "3":
        santiagoNum = int(input("Número para factorial: "))
        print("Resultado:", math.factorial(santiagoNum))
    else:
        print("Opción no válida")

santiagoCalcScience()
