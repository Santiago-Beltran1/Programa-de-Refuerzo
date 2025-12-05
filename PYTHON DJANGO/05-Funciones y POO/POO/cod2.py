class SantiagoBL:
    def __init__(self, SantiagoTit, SantiagoA):
        self.SantiagoTit = SantiagoTit
        self.SantiagoA = SantiagoA
        self.SantiagoDisp = True

    def SantiagoPres(self):
        if self.SantiagoDisp:
            self.SantiagoDisp = False
            return f"{self.SantiagoTit} ha sido prestado."
        else:
            return f"{self.SantiagoTit} no está disponible para préstamo."

    def SantiagoDev(self):
        if not self.SantiagoDisp:
            self.SantiagoDisp = True
            return f"{self.SantiagoTit} ha sido devuelto."
        else:
            return f"{self.SantiagoTit} ya está en la biblioteca."

    def SantiagoMost(self):
        SantiagoEst = "Disponible" if self.SantiagoDisp else "Prestado"
        return f"Libro: {self.SantiagoTit} de {self.SantiagoA} - Estado: {SantiagoEst}"

SantiagoLibro1 = SantiagoBL("Cóndores no Entierran Todos los Días", "Gustavo G.")
print(SantiagoLibro1.SantiagoMost())
print(SantiagoLibro1.SantiagoPres())
print(SantiagoLibro1.SantiagoMost())
print(SantiagoLibro1.SantiagoPres()) 
print(SantiagoLibro1.SantiagoDev())
print(SantiagoLibro1.SantiagoMost())
print(SantiagoLibro1.SantiagoDev())  

SantiagoLibro2 = SantiagoBL("Luna de Plutón", "Anónimo")
print(SantiagoLibro2.SantiagoMost())
print(SantiagoLibro2.SantiagoPres())
print(SantiagoLibro2.SantiagoMost())
