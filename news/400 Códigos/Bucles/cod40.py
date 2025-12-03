SantiagoBT = "David Santiago Beltran Pedraza"
SantiagoV = 0
for SantiagoL in SantiagoBT.lower():
    if SantiagoL in "aeiou":
        SantiagoV += 1
print("Cantidad de vocales:", SantiagoV)
