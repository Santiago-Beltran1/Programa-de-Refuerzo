class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoMos(self):
        print(f"Santiago: {self.Santiago}")

SantiagoList = [SantiagoB("Santiago1"), SantiagoB("Santiago2"), SantiagoB("Santiago3")]

for SantiagoO in SantiagoList:
    SantiagoO.SantiagoMos()
