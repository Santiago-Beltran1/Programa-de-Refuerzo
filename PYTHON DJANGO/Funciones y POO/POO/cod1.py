class SantiagoBP:
    def __init__(self, SantiagoTit, SantiagoGen, SantiagoD=0):
        self.SantiagoTit = SantiagoTit
        self.SantiagoGen = SantiagoGen
        self.SantiagoD = SantiagoD  
        self.SantiagoVisto = False

Santiago1 = SantiagoBP("Avengers", "Ciencia Ficción", 120)
Santiago2 = SantiagoBP("Dogs", "Animación", 95)

print(f"Pelicula titulada: {Santiago1.SantiagoTit} con duración de {Santiago1.SantiagoD} minutos") 
print(f"Pelicula titulada: {Santiago2.SantiagoTit} con duración de {Santiago2.SantiagoD} minutos")       