class SantiagoB:
    def __init__(self, SantiagoList):
        self.SantiagoList = SantiagoList

    def SantiagoFilter(self, SantiagoLimit):
        SantiagoFil = [x for x in self.SantiagoList if x > SantiagoLimit]
        print("Filtrada:", SantiagoFil)

Santiago1 = SantiagoB([51, 78, 5, 22])
Santiago1.SantiagoFilter(12)
