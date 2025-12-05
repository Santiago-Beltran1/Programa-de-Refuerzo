class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def __del__(self):
        print(f"Objeto {self.Santiago} eliminado")

SantiagoObj = SantiagoB("Santiago")
del SantiagoObj
