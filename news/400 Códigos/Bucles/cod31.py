SantiagoB = [10, 4, 18, 5.4, 44.4, 45]

SantiagoSum = sum(SantiagoB)
SantiagoMed = SantiagoSum / len(SantiagoB)
SantiagoVari = sum((x - SantiagoMed) ** 2 for x in SantiagoB) / len(SantiagoB)
SantiagoDesv = SantiagoVari ** 0.5

print(f"En la lista - La suma = {SantiagoSum} - La Media = {SantiagoMed} - La Varianza =  {SantiagoDesv} - La Desviación = {SantiagoDesv}")
