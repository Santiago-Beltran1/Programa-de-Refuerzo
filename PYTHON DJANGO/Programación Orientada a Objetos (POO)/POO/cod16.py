class SantiagoRobot:
    def __init__(self, SantiagoNom, SantiagoModelo):
        self.santiago_nom = SantiagoNom      
        self.santiago_modelo = SantiagoModelo 
        self.santiago_estado = "Activo"       
    def SantiagoCargBat(self):
        self.santiago_estado = "Cargado"
        return f"{self.santiago_nom} ha sido cargado y ahora está {self.santiago_estado}."

    def SantiagoRTarea(self):
        self.santiago_estado = "Trabajando"
        return f"{self.santiago_nom} está realizando su tarea y ahora está {self.santiago_estado}."

    def SantiagoReposo(self):
        self.santiago_estado = "Reposo"
        return f"{self.santiago_nom} ha entrado en modo reposo y ahora está {self.santiago_estado}."

    def SantiagoEstado(self):
        return f"{self.santiago_nom}, modelo {self.santiago_modelo}, está {self.santiago_estado}."


# Uso de la clase SantiagoRobot con valores distintos
santiagoR1 = SantiagoRobot("RoboMax", "RX-2025")
print(santiagoR1.SantiagoEstado())
print(santiagoR1.SantiagoCargBat())
print(santiagoR1.SantiagoEstado())
print(santiagoR1.SantiagoRTarea())
print(santiagoR1.SantiagoEstado())
print(santiagoR1.SantiagoReposo())
print(santiagoR1.SantiagoEstado())
print(santiagoR1.SantiagoCargBat())  

santiagoR2 = SantiagoRobot("Lumi", "LX-900")
print(santiagoR2.SantiagoEstado())
print(santiagoR2.SantiagoRTarea())
print(santiagoR2.SantiagoReposo())
print(santiagoR2.SantiagoEstado())
