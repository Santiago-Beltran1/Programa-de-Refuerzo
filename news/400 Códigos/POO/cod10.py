class SantiagoBEst:
    def __init__(self, SantiagoNom, SantiagoID):
        self.SantiagoNom = SantiagoNom
        self.SantiagoID = SantiagoID
        self.SantiagoPuns = []

    def SantiagoAg(self, SantiagoPun):
        if 0 <= SantiagoPun <= 100:
            self.SantiagoPuns.append(SantiagoPun)
            return f"Calificación {SantiagoPun} agregada a {self.SantiagoNom}."
        else:
            return "Calificación inválida, debe estar entre 0 y 100."

    def SantiagoProm(self):
        if not self.SantiagoPuns:
            return "El estudiante aún no tiene calificaciones."
        return sum(self.SantiagoPuns) / len(self.SantiagoPuns)

    def SantiagoInf(self):
        SantiagoPromDef = self.SantiagoProm()
        if isinstance(SantiagoPromDef, float):
            SantiagoStr = f"{SantiagoPromDef:.2f}"
        else:
            SantiagoStr = SantiagoPromDef
        return f"Estudiante: {self.SantiagoNom}, ID: {self.SantiagoID}, Calificaciones: {self.SantiagoPuns}, Promedio: {SantiagoStr}"

Santiago1 = SantiagoBEst("David Beltran", "C2")
print(Santiago1.SantiagoInf())
print(Santiago1.SantiagoAg(3.5))
print(Santiago1.SantiagoAg(2.6))
print(Santiago1.SantiagoAg(5.0))
print(Santiago1.SantiagoAg(4.1))  
print(Santiago1.SantiagoInf())
print(f"Promedio de {Santiago1.SantiagoNom}: {Santiago1.SantiagoProm():.2f}")

Santiago2 = SantiagoBEst("Santiago Pedraza", "C1")
print(Santiago2.SantiagoAg(3.0))
print(Santiago2.SantiagoAg(1))
print(Santiago2.SantiagoInf())
