import random as SantiagoRandom

def SantiagoGen(SantiagoEmp):
    SantiagoDias = ["Lunes","Martes","Miércoles","Jueves","Viernes"]
    SantiagoHorario = {}
    for SantiagoEmpleado in SantiagoEmp:
        SantiagoHorario[SantiagoEmpleado] = {dia: f"{SantiagoRandom.randint(8,12)}:00-{SantiagoRandom.randint(13,18)}:00" for dia in SantiagoDias}
    for SantiagoEmpleado, SantiagoDiasHorario in SantiagoHorario.items():
        print(f"Horario de {SantiagoEmpleado}:")
        for SantiagoD, SantiagoH in SantiagoDiasHorario.items():
            print(f"  {SantiagoD}: {SantiagoH}")
        print("-"*30)

SantiagoGen(["David","Santiago"])
