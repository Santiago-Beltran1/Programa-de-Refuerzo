class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoPrimo(self, SantiagoN):
        if SantiagoN < 2:
            return False
        for SantiagoI in range(2, int(SantiagoN ** 0.5) + 1):
            if SantiagoN % SantiagoI == 0:
                return False
        return True

Santiago1 = SantiagoB("Números Primos")
print(f"7 es primo Santiago: {Santiago1.SantiagoPrimo(7)}")
print(f"15 es primo Santiago: {Santiago1.SantiagoPrimo(15)}")
