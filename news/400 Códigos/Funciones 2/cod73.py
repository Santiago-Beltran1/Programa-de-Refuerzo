import time as SantiagoTime

class SantiagoRe:
    def __init__(self, SantiagoMens, SantiagoSegs):
        self.SantiagoMensaje = SantiagoMens
        self.SantiagoSegundos = SantiagoSegs

    def SantiagoActi(self):
        print(f"Recordatorio activado: '{self.SantiagoMensaje}' en {self.SantiagoSegundos} segundos...")
        SantiagoTime.sleep(self.SantiagoSegundos)
        print(f"ALERTA: {self.SantiagoMensaje}")

Santiago1 = SantiagoRe("Revisar correo:", 3)
Santiago1.SantiagoActi()
