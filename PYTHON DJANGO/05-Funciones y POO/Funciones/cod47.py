def SantiagoBisiesto(SantiagoAño):
    return SantiagoAño % 4 == 0 and (SantiagoAño % 100 != 0 or SantiagoAño % 400 == 0)

def SantiagoMain():
    try:
        SantiagoA = int(input("Ingresa un año: "))
        print("Es bisiesto" if SantiagoBisiesto(SantiagoA) else "No es bisiesto")
    except:
        print("Número inválido.")

SantiagoMain()
