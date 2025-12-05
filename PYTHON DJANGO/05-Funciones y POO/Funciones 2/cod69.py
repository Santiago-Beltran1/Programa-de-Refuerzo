from collections import deque as SantiagoDeque

class SantiagoAt:
    def __init__(self):
        self.SantiagoClientes = SantiagoDeque()

    def SantiagoAg(self, SantiagoNom):
        self.SantiagoClientes.append(SantiagoNom)

    def SantiagoAtend(self):
        if self.SantiagoClientes:
            return self.SantiagoClientes.popleft()
        return "SantiagoNo hay clientes"

Santiago1 = SantiagoAt()
Santiago1.SantiagoAg("SantiagoB")
Santiago1.SantiagoAg("SantiagoP")
print(Santiago1.SantiagoAtend())
print(Santiago1.SantiagoAtend())
