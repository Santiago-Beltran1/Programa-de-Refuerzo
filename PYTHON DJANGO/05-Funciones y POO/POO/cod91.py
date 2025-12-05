class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoSumM(self, SantiagoA, SantiagoB):
        SantiagoR = [[SantiagoA[SantiagoI][SantiagoJ] + SantiagoB[SantiagoI][SantiagoJ] for SantiagoJ in range(len(SantiagoA[0]))] for SantiagoI in range(len(SantiagoA))]
        return SantiagoR

Santiago1 = SantiagoB("Suma de matrices")
matriz1 = [[1,2],[3,4]]
matriz2 = [[5,6],[7,8]]
print(f"Suma de matrices: {Santiago1.SantiagoSumM(matriz1, matriz2)}")
