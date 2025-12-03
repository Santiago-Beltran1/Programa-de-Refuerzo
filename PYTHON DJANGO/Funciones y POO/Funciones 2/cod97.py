class SantiagoHrs:
    def __init__(self):
        self.SantiagoRegis = []

    def SantiagoAg(self, SantiagoEmpleado, SantiagoHorasTrabajadas):
        self.SantiagoRegis.append({"empleado":SantiagoEmpleado,"horas":SantiagoHorasTrabajadas})
        print(f"Horas agregadas: {SantiagoEmpleado} - {SantiagoHorasTrabajadas}h")

    def SantiagoRepor(self):
        print("Reporte de horas trabajadas:")
        for r in self.SantiagoRegis:
            print(f"  {r['empleado']}: {r['horas']} horas")

SantiagoT1 = SantiagoHrs()
SantiagoT1.SantiagoAg("David",9)
SantiagoT1.SantiagoAg("Santiago",12)
SantiagoT1.SantiagoRepor()
