import random as SantiagoRandom

def SantiagoGen(SantiagoEst, SantiagoMat):
    for estudiante in SantiagoEst:
        SantiagoHorario = {materia: f"{SantiagoRandom.randint(8,17)}:00-{SantiagoRandom.randint(18,20)}:00" for materia in SantiagoMat}
        print(f"Horario de {estudiante}:")
        for SantiagoM, SantiagoH in SantiagoHorario.items():
            print(f"  {SantiagoM}: {SantiagoH}")
        print("-"*30)

SantiagoGen(["David","Santiago"],["Django","Frontend","SQL"])
