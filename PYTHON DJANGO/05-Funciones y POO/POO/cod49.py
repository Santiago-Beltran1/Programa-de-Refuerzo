class SantiagoB:
    SantiagoTasks = []

    def __init__(self, SantiagoT):
        self.SantiagoT = SantiagoT
        SantiagoB.SantiagoTasks.append(SantiagoT)

    @classmethod
    def mostrarTareas(cls):
        print("Tareas pendientes:", cls.SantiagoTasks)

    @classmethod
    def SantiagoEli(cls, SantiagoT):
        if SantiagoT in cls.SantiagoTasks:
            cls.SantiagoTasks.remove(SantiagoT)
            print(f"Tarea '{SantiagoT}' eliminada")
        else:
            print("Tarea no encontrada")

Santiago1 = SantiagoB("Comprar comida")
Santiago2 = SantiagoB("Llamar al doctor")
SantiagoB.mostrarTareas()
SantiagoB.SantiagoEli("Comprar comida")
SantiagoB.mostrarTareas()
