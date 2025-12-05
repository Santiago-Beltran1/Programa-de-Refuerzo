class SantiagoB:
    def __init__(self, Santiago):
        self.__Santiago = Santiago  

    def Santiagoget(self):
        return self.__Santiago

    def setSantiago(self, Santiago):
        self.__Santiago = Santiago

SantiagoObj = SantiagoB("Inicial")
print(SantiagoObj.Santiagoget())
SantiagoObj.setSantiago("Modificado")
print(SantiagoObj.Santiagoget())
