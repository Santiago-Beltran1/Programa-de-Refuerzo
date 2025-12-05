def SantiagoFibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci.

    Args:
        n (int): Posición en la secuencia (empezando por 0).

    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return SantiagoFibonacci(n - 1) + SantiagoFibonacci(n - 2)

for i in range(10):
    print(SantiagoFibonacci(i), end=" ")
