import time

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoTemporizar(self, SantiagoSegundos):
        print(f"Temporizador Santiago iniciado por {SantiagoSegundos} segundos")
        time.sleep(SantiagoSegundos)
        print("Tiempo Santiago terminado!")

Santiago1 = SantiagoB("Temporizador")
Santiago1.SantiagoTemporizar(3)
