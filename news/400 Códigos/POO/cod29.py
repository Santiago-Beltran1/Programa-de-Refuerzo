class SantiagoB:
    def SantiagoOpera(self, SantiagoA, SantiagoB):
        raise NotImplementedError("Las subclases deben implementar 'SantiagoOpera()'")

class SantiagoSum(SantiagoB):
    def SantiagoOpera(self, SantiagoA, SantiagoB):
        resultado = SantiagoA + SantiagoB
        return f"Suma: {SantiagoA} + {SantiagoB} = {resultado}"

class SantiagoRes(SantiagoB):
    def SantiagoOpera(self, SantiagoA, SantiagoB):
        resultado = SantiagoA - SantiagoB
        return f"Resta: {SantiagoA} - {SantiagoB} = {resultado}"

class SantiagoMul(SantiagoB):
    def SantiagoOpera(self, SantiagoA, SantiagoB):
        SantiagoR = SantiagoA * SantiagoB
        return f"Multiplicación: {SantiagoA} × {SantiagoB} = {SantiagoR}"

class SantiagoDiv(SantiagoB):
    def SantiagoOpera(self, SantiagoA, SantiagoB):
        if SantiagoB == 0:
            return "Error: División por cero no permitida."
        resultado = SantiagoA / SantiagoB
        return f"División: {SantiagoA} ÷ {SantiagoB} = {resultado}"

def SantiagoVer(operacion, SantiagoA, SantiagoB):
    print(operacion.SantiagoOpera(SantiagoA, SantiagoB))

SantiagoS = SantiagoSum()
SantiagoRdor = SantiagoRes()
SantiagoM = SantiagoMul()
SantiagoD = SantiagoDiv()

SantiagoVer(SantiagoS, 100, 5)
SantiagoVer(SantiagoRdor, 100, 5)
SantiagoVer(SantiagoM, 100, 5)
SantiagoVer(SantiagoD, 100, 5)
SantiagoVer(SantiagoD, 100, 0)  

SantiagoOprcns = [SantiagoSum(), SantiagoRes(), SantiagoMul(), SantiagoDiv()]
print("\nProbando todas las operaciones polimórficamente:")
for SantiagoOp in SantiagoOprcns:
    SantiagoVer(SantiagoOp, 7, 3)
