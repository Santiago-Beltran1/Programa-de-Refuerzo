class Santiago:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoParImpar(self, SantiagoNumero):
        return "Par Santiago" if SantiagoNumero % 2 == 0 else "Impar Santiago"

# Uso
SantiagoObj = Santiago("ParImparSantiago")
print("7 Santiago =", SantiagoObj.SantiagoParImpar(7))
print("10 Santiago =", SantiagoObj.SantiagoParImpar(10))
