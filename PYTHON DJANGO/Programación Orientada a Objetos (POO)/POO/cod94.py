class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoFibonacci(self, SantiagoN):
        SantiagoSeq = [0,1]
        for _ in range(2, SantiagoN):
            SantiagoSeq.append(SantiagoSeq[-1] + SantiagoSeq[-2])
        return SantiagoSeq[:SantiagoN]

Santiago1 = SantiagoB("Fibonacci Secuencia")
print(f"Fibonacci: {Santiago1.SantiagoFibonacci(10)}")
