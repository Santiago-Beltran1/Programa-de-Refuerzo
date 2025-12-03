class SantiagoB:
    SantiagoRegis = []  

    def __init__(self, Santiago):
        self.Santiago = Santiago  
        SantiagoB.SantiagoRegis.append(Santiago)  

    @classmethod
    def SantiagoMos(cls):
        print("Usuarios registrados:", cls.SantiagoRegis)

Santiago1 = SantiagoB("David")
Santiago2 = SantiagoB("Beltran")

SantiagoB.SantiagoMos()
