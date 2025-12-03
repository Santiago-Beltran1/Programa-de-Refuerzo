def SantiagoIMC(SantiagoPeso, SantiagoAltura):
    return SantiagoPeso / (SantiagoAltura ** 2)

def SantiagoMain():
    try:
        SantiagoPeso = float(input("Peso (kg): "))
        SantiagoAltura = float(input("Altura (m): "))
        print(f"Tu IMC es: {SantiagoIMC(SantiagoPeso, SantiagoAltura):.2f}")
    except:
        print("Error en los datos.")

SantiagoMain()
