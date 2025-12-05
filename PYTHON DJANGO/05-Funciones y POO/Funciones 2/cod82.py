class SantiagoEncues:
    def __init__(self, SantiagoPregunt):
        self.SantiagoPreguntas = SantiagoPregunt
        self.SantiagoR = {preg:[] for preg in SantiagoPregunt}

    def SantiagoResponder(self, SantiagoRDict):
        for preg, resp in SantiagoRDict.items():
            if preg in self.SantiagoR:
                self.SantiagoR[preg].append(resp)
        print(f"Respuestas registradas: {SantiagoRDict}")

    def SantiagoMos(self):
        print("Resultados de la encuesta:")
        for SantiagoPreg, SantiagoResp in self.SantiagoR.items():
            print(f"  {SantiagoPreg}: {SantiagoResp}")

Santiago1 = SantiagoEncues(["Azul", "Rojo", "Amarillo"])
Santiago1.SantiagoResponder({"Azul":"Sí", "Amarillo":"No"})
Santiago1.SantiagoMos()
