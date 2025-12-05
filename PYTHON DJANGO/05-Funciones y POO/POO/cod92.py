class SantiagoBT:
    def __init__(self, SantiagoDesc):
        self.SantiagoDesc = SantiagoDesc
        self.SantiagoCompletada = False

    def SantiagoCompletar(self):
        self.SantiagoCompletada = True

class SantiagoList:
    def __init__(self):
        self.SantiagoTareas = []

    def SantiagoAg(self, SantiagoTarea):
        self.SantiagoTareas.append(SantiagoTarea)

    def SantiagoMostrarPendientes(self):
        return [t.SantiagoDesc for t in self.SantiagoTareas if not t.SantiagoCompletada]

Santiago1 = SantiagoBT("Ir al GYM")
Santiago2 = SantiagoBT("Hacer los 400 ejercicios")
SantiagoL1 = SantiagoList()
SantiagoL1.SantiagoAg(Santiago1)
SantiagoL1.SantiagoAg(Santiago2)

Santiago1.SantiagoCompletar()

pendientes = SantiagoL1.SantiagoMostrarPendientes()
print(f"Tareas pendientes ({len(pendientes)}): {pendientes}")
