def SantiagoEsPrimo(SantiagoN):
    if SantiagoN < 2:
        return False
    for SantiagoI in range(2, int(SantiagoN ** 0.5) + 1):
        if SantiagoN % SantiagoI == 0:
            return False
    return True

def SantiagoMain():
    try:
        SantiagoN = int(input("Número para verificar: "))
        print("Es primo" if SantiagoEsPrimo(SantiagoN) else "No es primo")
    except ValueError:
        print("Número inválido.")

SantiagoMain()
