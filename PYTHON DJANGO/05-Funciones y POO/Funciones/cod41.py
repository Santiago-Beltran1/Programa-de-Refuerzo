def SantiagoEdadEnDias(SantiagoAnios):
    return SantiagoAnios * 365

def SantiagoMain():
    try:
        SantiagoEdad = int(input("Ingresa tu edad en años: "))
        print(f"Tienes aproximadamente {SantiagoEdadEnDias(SantiagoEdad)} días de vida.")
    except ValueError:
        print("Edad inválida.")

SantiagoMain()
