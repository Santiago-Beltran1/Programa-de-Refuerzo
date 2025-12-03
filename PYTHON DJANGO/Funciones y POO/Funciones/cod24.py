import math

def SantiagoB_CalArea(SantiagoRadio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return math.pi * SantiagoRadio ** 2

# Mostramos documentación de la función
help(SantiagoB_CalArea)
print(SantiagoB_CalArea.__doc__)

SantiagoRad = float(input("Ingresa el radio del círculo: "))
SantiagoArea = SantiagoB_CalArea(SantiagoRad)
print(f"El área del círculo con radio {SantiagoRad} es: {SantiagoArea:.2f}cm^2")
