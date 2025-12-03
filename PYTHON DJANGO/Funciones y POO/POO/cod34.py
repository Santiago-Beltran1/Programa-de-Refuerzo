class SantiagoB:
    SantiagoCont = 0 

    def __init__(self, Santiago):
        self.Santiago = Santiago
        SantiagoB.SantiagoCont += 1  

    @classmethod
    def SantiagoMos(cls):
        print(f"Se han creado {cls.SantiagoCont} objetos Santiago")

Santiago1 = SantiagoB("Santiago1")
Santiago2 = SantiagoB("Santiago2")

SantiagoB.SantiagoMos()
