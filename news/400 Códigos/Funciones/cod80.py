def SantiagoBDiaSemana(SantiagoBDia, SantiagoBMes, SantiagoBAnio):
    if SantiagoBMes < 3:
        SantiagoBMes += 12
        SantiagoBAnio -= 1
    SantiagoK = SantiagoBAnio % 100
    Santiagoj = SantiagoBAnio // 100
    SantiagoH = (SantiagoBDia + (13*(SantiagoBMes+1))//5 + SantiagoK + SantiagoK//4 + Santiagoj//4 + 5*Santiagoj) % 7
    SantiagoD = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    return SantiagoD[SantiagoH]

SantiagoDi = int(input("Día: "))
SantiagoM = int(input("Mes: "))
SantiagoA = int(input("Año: "))
print("Ese día fue:", SantiagoBDiaSemana(SantiagoDi, SantiagoM, SantiagoA))
