SantiagoP = float(input("Presupuesto semanal: "))
SantiagoGast = 0
SantiagoB = ""

while SantiagoGast < SantiagoP:
    SantiagoB = input("Ingrese gasto o 'fin': ").lower()
    if SantiagoB=="fin":
        break
    SantiagoGasto = float(SantiagoB)
    if SantiagoGast + SantiagoGasto <= SantiagoP:
        SantiagoGast += SantiagoGasto
        print("Gasto registrado, saldo restante:", SantiagoP - SantiagoGast)
    else:
        print("Excede el presupuesto")
