def SantiagoSum(SantiagoA, SantiagoB):
    return SantiagoA + SantiagoB

def SantiagoRes(SantiagoA, SantiagoB):
    return SantiagoA - SantiagoB

def SantiagoMul(SantiagoA, SantiagoB):
    return SantiagoA * SantiagoB

def SantiagoDiv(SantiagoA, SantiagoB):
    if SantiagoB == 0:
        return "Error: División entre cero no permitida"
    return SantiagoA / SantiagoB

def SantiagoCalc():
    print("Calculadora simple")
    print("Elige la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    SantiagoOpc = input("Ingresa el número de la operación (1/2/3/4): ")

    if SantiagoOpc not in ['1', '2', '3', '4']:
        print("Opción inválida")
        return

    try:
        SantiagoN1 = float(input("Ingresa el primer número: "))
        SantiagoN2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Debes ingresar números válidos")
        return

    if SantiagoOpc == '1':
        SantiagoR = SantiagoSum(SantiagoN1, SantiagoN2)
    elif SantiagoOpc == '2':
        SantiagoR = SantiagoRes(SantiagoN1, SantiagoN2)
    elif SantiagoOpc == '3':
        SantiagoR = SantiagoMul(SantiagoN1, SantiagoN2)
    elif SantiagoOpc == '4':
        SantiagoR = SantiagoDiv(SantiagoN1, SantiagoN2)

    print(f"El resultado es: {SantiagoR}")

SantiagoCalc()
