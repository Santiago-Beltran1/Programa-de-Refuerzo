from datetime import datetime

def SantiagoDiasVividos(SantiagoNacimiento):
    SantiagoHoy = datetime.now()
    SantiagoFechaN = datetime.strptime(SantiagoNacimiento, "%d/%m/%Y")
    return (SantiagoHoy - SantiagoFechaN).days

def SantiagoMain():
    try:
        SantiagoFecha = input("Ingresa tu fecha de nacimiento (dd/mm/yyyy): ")
        print(f"Has vivido {SantiagoDiasVividos(SantiagoFecha)} días aproximadamente.")
    except:
        print("Formato de fecha inválido.")

SantiagoMain()
