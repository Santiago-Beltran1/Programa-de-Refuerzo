class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoFacto(self, SantiagoN):
        SantiagoR = 1
        for SantiagoI in range(1, SantiagoN + 1):
            SantiagoR *= SantiagoI
        return SantiagoR

Santiago1 = SantiagoB("Factorial")
print(f"7! Santiago = {Santiago1.SantiagoFacto(7)}")
