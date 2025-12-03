from datetime import datetime

def SantiagoFechaHora():
    SantiagoActual = datetime.now()
    print("Fecha y hora actual:", SantiagoActual.strftime("%d/%m/%Y %H:%M:%S"))

SantiagoFechaHora()
