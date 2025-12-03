import math

def SantiagoB_CalArea(SantiagoRadio):
    """
    Calcula el área de un círculo.
    """
    return math.pi * SantiagoRadio ** 2

SantiagoR = SantiagoB_CalArea(10)
print(f"El círculo tiene {SantiagoR}cm^2 de área")
