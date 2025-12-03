def SantiagoB_GenFibonacci(Santiagolimit):
    """
    Generador que produce números de Fibonacci hasta un límite.

    Args:
        limite (int): Valor máximo a generar.
    """
    SantiagoA, SantiagoB = 0, 1
    while SantiagoA < Santiagolimit:
        yield SantiagoA
        SantiagoA, SantiagoB = SantiagoB, SantiagoA + SantiagoB

for SantiagoN in SantiagoB_GenFibonacci(50):
    print(SantiagoN, end=" ") 
