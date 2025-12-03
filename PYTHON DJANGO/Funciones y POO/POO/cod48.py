class SantiagoB:
    SantiagoRegis = []

    def __init__(self, Santiago):
        self.Santiago = Santiago
        SantiagoB.SantiagoRegis.append(Santiago)

    def SantiagoActu(self, SantiagoNew):
        if self.Santiago in SantiagoB.SantiagoRegis:
            idx = SantiagoB.SantiagoRegis.index(self.Santiago)
            SantiagoB.SantiagoRegis[idx] = SantiagoNew
            self.Santiago = SantiagoNew
            print(f"Nombre actualizado a {SantiagoNew}")

Santiago1 = SantiagoB("Santiago")
Santiago1.SantiagoActu("David")
print(SantiagoB.SantiagoRegis)
