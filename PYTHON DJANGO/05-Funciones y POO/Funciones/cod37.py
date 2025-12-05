def SantiagoMetrosAKm(SantiagoMetros):
    return SantiagoMetros / 1000

def SantiagoMain():
    try:
        SantiagoM = float(input("Ingresa metros: "))
        print(f"{SantiagoM} metros = {SantiagoMetrosAKm(SantiagoM)} km")
    except ValueError:
        print("Entrada inválida.")

SantiagoMain()
