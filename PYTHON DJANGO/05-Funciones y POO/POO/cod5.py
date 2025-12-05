class SantiagoBEmp:
    def __init__(self, SantiagoNom, SantiagoPuesto, SantiagoSalarioMensual):
        self.santiago_nom = SantiagoNom
        self.santiago_puesto = SantiagoPuesto
        self.santiago_salario_mensual = SantiagoSalarioMensual

    def SantiagoObtSal(self):
        return self.santiago_salario_mensual * 12

    def SantiagoApliAu(self, SantiagoPorcentaje):
        if 0 < SantiagoPorcentaje <= 100:
            aumento = self.santiago_salario_mensual * (SantiagoPorcentaje / 100)
            self.santiago_salario_mensual += aumento
            return f"Salario de {self.santiago_nom} aumentado en {SantiagoPorcentaje}%. Nuevo salario mensual: ${self.santiago_salario_mensual:.2f}."
        else:
            return "El porcentaje de aumento debe estar entre 0 y 100."

    def SantiagoInfo(self):
        return (f"Empleado: {self.santiago_nom} | Puesto: {self.santiago_puesto} | "
                f"Salario Mensual: ${self.santiago_salario_mensual:.2f} | "
                f"Salario Anual: ${self.SantiagoObtSal():.2f}")


santiago1 = SantiagoBEmp("Santiago Beltran", "Analista", 3200000)
print(santiago1.SantiagoInfo())
print(santiago1.SantiagoApliAu(12))  
print(santiago1.SantiagoInfo())
print(santiago1.SantiagoApliAu(7))   
print(santiago1.SantiagoInfo())
print(santiago1.SantiagoApliAu(-5)) 

santiago2 = SantiagoBEmp("David Pedraza", "Ingeniero", 2800000)
print(santiago2.SantiagoInfo())
print(santiago2.SantiagoApliAu(10))
print(santiago2.SantiagoInfo())
