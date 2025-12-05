class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoSum(self, Santiago, Santiago2):
        return Santiago + Santiago2

SantiagoObj = SantiagoB("Santiago")
SantiagoR = SantiagoObj.SantiagoSum(74, 110)
print(f"La suma es igual a: {SantiagoR}")
