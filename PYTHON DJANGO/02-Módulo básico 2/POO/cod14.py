class SantiagoB:
    def __init__(self):
        pass 

    def SantiagoSum(self, SantiagoN1, SantiagoN2):
        return SantiagoN1 + SantiagoN2

    def SantiagoRes(self, SantiagoN1, SantiagoN2):
        return SantiagoN1 - SantiagoN2

    def SantiagoMul(self, SantiagoN1, SantiagoN2):
        return SantiagoN1 * SantiagoN2

    def SantiagoDiv(self, SantiagoN1, SantiagoN2):
        if SantiagoN2 != 0:
            return SantiagoN1 / SantiagoN2
        else:
            return "Error División por cero no permitida."

SantiagoCalc = SantiagoB()
print(f"La suma de 100 + 200 es = {SantiagoCalc.SantiagoSum(100, 200)}")
print(f"La resta de 15 - 7 es = {SantiagoCalc.SantiagoRes(15, 7)}")
print(f"La multiplicación de 5 * 5 = {SantiagoCalc.SantiagoMul(5, 5)}")
print(f"La división de 100 / 3 = {SantiagoCalc.SantiagoDiv(100, 3)}")
print(f"La división de 11 / 0 = {SantiagoCalc.SantiagoDiv(11, 0)}")
