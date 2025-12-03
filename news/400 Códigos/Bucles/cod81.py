SantiagoB = input("Ingrese una frase: ").lower()
SantiagoP = SantiagoB.split()
SantiagoFrec = {}

for SantiagoP in SantiagoP:
    SantiagoFrec[SantiagoP] = SantiagoFrec.get(SantiagoP, 0) + 1

print(f"la frecuencia de palabras fue de: {SantiagoFrec}")
