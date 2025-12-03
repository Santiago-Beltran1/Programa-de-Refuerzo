import statistics

SantiagoLis = []
SantiagoB = ""

while SantiagoB != "fin":
    SantiagoB = input("Ingrese número o 'fin': ").lower()
    if SantiagoB != "fin":
        SantiagoLis.append(float(SantiagoB))

if SantiagoLis:
    print(f"Media: {statistics.mean(SantiagoLis)}")
    print(f"Mediana: {statistics.median(SantiagoLis)}")
    print(f"Desviación estándar: {statistics.stdev(SantiagoLis) if len(SantiagoLis)>1 else 0}")