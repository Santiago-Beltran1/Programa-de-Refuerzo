import datetime

SantiagoFechas = []
SantiagoB = ""

while SantiagoB != "fin":
    SantiagoB = input("Ingrese fecha Año/Mes/Día o 'fin': ").lower()
    if SantiagoB != "fin":
        SantiagoFecha = datetime.datetime.strptime(SantiagoB, "%Y-%m-%d").date()
        SantiagoFechas.append(SantiagoFecha)

for SantiagoF in sorted(SantiagoFechas):
    print(f"Fecha registrada: {SantiagoF}")
