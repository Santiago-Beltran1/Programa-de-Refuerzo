import random

class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoGenHorario(self, SantiagoActi):
        SantiagoD = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        SantiagoHorario = {}
        for SantiagoDia in SantiagoD:
            SantiagoActividad = random.choice(SantiagoActi)
            SantiagoHorario[SantiagoDia] = SantiagoActividad
        return SantiagoHorario

Santiago1 = SantiagoB("Creador de Horario")
SantiagoH = Santiago1.SantiagoGenHorario(["Estudio", "Deporte", "Descanso", "Trabajo"])
print(SantiagoH)
