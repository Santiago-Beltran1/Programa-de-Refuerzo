from datetime import datetime as SantiagoDatetime

def SantiagoComp(SantiagoFecha):
    SantiagoHoy = SantiagoDatetime.now()
    if (SantiagoFecha.month, SantiagoFecha.day) == (SantiagoHoy.month, SantiagoHoy.day):
        return "Feliz cumpleaños!"
    return "Hoy no cumple años."

SantiagoF = SantiagoDatetime(2007, 10, 19)
print(SantiagoComp(SantiagoF))
