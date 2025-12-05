class SantiagoCalculadora:
    def __init__(self):
        pass  # La calculadora no necesita atributos iniciales

    def SantiagoSumar(self, santiagoA, santiagoB):
        return santiagoA + santiagoB

    def SantiagoRestar(self, santiagoA, santiagoB):
        return santiagoA - santiagoB

    def SantiagoMultiplicar(self, santiagoA, santiagoB):
        return santiagoA * santiagoB

    def SantiagoDividir(self, santiagoA, santiagoB):
        if santiagoB != 0:
            return santiagoA / santiagoB
        else:
            return "Error: División por cero no permitida."


santiagoCalc = SantiagoCalculadora()

print(f"8 + 12 = {santiagoCalc.SantiagoSumar(8, 12)}")
print(f"15 - 7 = {santiagoCalc.SantiagoRestar(15, 7)}")
print(f"9 * 5 = {santiagoCalc.SantiagoMultiplicar(9, 5)}")
print(f"36 / 6 = {santiagoCalc.SantiagoDividir(36, 6)}")
print(f"10 / 0 = {santiagoCalc.SantiagoDividir(10, 0)}")
