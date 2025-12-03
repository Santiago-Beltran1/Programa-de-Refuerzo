# CLASE BASE
class SantiagoBEmpl:
    """Clase base para todos los empleados"""
    
    # Atributo de clase
    santiago_empresa = "SENA Mosquera - CBA"

    def __init__(self, santiago_nom, santiago_id, santiago_salario):
        self.santiago_nom = santiago_nom
        self.santiago_id = santiago_id
        self.santiago_salario = santiago_salario
        self.santiago_horas = 0

    def SantiagoRegis(self, horas):
        self.santiago_horas += horas
        return f"{self.santiago_nom} trabajó {horas} horas"

    def santiago_calcSal(self):
        return self.santiago_salario

    def __str__(self):
        return f"{self.santiago_nom} - ID: {self.santiago_id}"


# CLASE HIJA - INSTRUCTOR
class SantiagoInstructor(SantiagoBEmpl):
    """Instructor del SENA - Hereda de Empleado"""

    def __init__(self, santiago_nom, santiago_id, santiago_salario, santiago_especialidad):
        super().__init__(santiago_nom, santiago_id, santiago_salario)
        self.santiago_especialidad = santiago_especialidad
        self.santiago_cursos = []
        self.santiago_estudiantes = 0

    def santiagoAsigCurs(self, curso):
        self.santiago_cursos.append(curso)
        return f"Curso '{curso}' asignado a {self.santiago_nom}"

    def santiago_calcSal(self):
        bonus_cursos = len(self.santiago_cursos) * 200000
        bonus_estudiantes = self.santiago_estudiantes * 5000
        return self.santiago_salario + bonus_cursos + bonus_estudiantes

    def __str__(self):
        return f"Instructor {super().__str__()} - {self.santiago_especialidad}"


# CLASE HIJA - ADMINISTRATIVO
class SantiagoAdministrativo(SantiagoBEmpl):
    """Personal administrativo - Hereda de Empleado"""

    def __init__(self, santiago_nom, santiago_id, santiago_salario, santiago_dpto):
        super().__init__(santiago_nom, santiago_id, santiago_salario)
        self.santiago_dpto = santiago_dpto
        self.santiago_proyectos = 0

    def santiagoComplProy(self, proyecto):
        self.santiago_proyectos += 1
        return f"Proyecto '{proyecto}' completado por {self.santiago_nom}"

    def santiago_calcSal(self):
        bonus = self.santiago_proyectos * 150000
        return self.santiago_salario + bonus

    def __str__(self):
        return f"Administrativo {super().__str__()} - Dpto. {self.santiago_dpto}"


# DEMOSTRACIÓN
print("=== SISTEMA DE EMPLEADOS ===\n")

# Crear empleados
SantiagoIns1 = SantiagoInstructor("David Beltran", "ID001", 2000000, "Programación Python")
SantiagoIns2 = SantiagoInstructor("Santiago Pedraza", "ID002", 5500000, "Bases de Datos")
SantiagoAd1 = SantiagoAdministrativo("David Santiago", "ID003", 2300000, "Frontend")

# Asignar trabajo
print(SantiagoIns1.santiagoAsigCurs("POO en Python"))
print(SantiagoIns1.santiagoAsigCurs("Django Avanzado"))
SantiagoIns1.santiago_estudiantes = 45

print(SantiagoIns2.santiagoAsigCurs("SQL Básico"))
SantiagoIns2.santiago_estudiantes = 30

print(SantiagoAd1.santiagoComplProy("Sistema de Nómina"))
print(SantiagoAd1.santiagoComplProy("Portal de Inscripciones"))

SantiagoIns1.SantiagoRegis(40)
SantiagoAd1.SantiagoRegis(38)

print("\n=== SALARIOS DEL MES ===")
print(f"{SantiagoIns1.santiago_nom}: ${SantiagoIns1.santiago_calcSal():,}")
print(f"{SantiagoIns2.santiago_nom}: ${SantiagoIns2.santiago_calcSal():,}")
print(f"{SantiagoAd1.santiago_nom}: ${SantiagoAd1.santiago_calcSal():,}")
