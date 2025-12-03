import random as SantiagoRandom

def SantiagoPlan(SantiagoDias, SantiagoMaterias):
    SantiagoPlan = {}
    for SantiagoDia in SantiagoDias:
        SantiagoPlan[SantiagoDia] = SantiagoRandom.choice(SantiagoMaterias)
    return SantiagoPlan

SantiagoDias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
SantiagoMaterias = ["Estudiar", "GYM", "Leer", "Caminata"]
print(SantiagoPlan(SantiagoDias, SantiagoMaterias))
