#Imprimir una lista sin que se repita un valor

santiagoN = [1, 2, 2, 3, 4, 4, 5]
santiagoNDups = []
for santiagoNum in santiagoN:
    if santiagoNum not in santiagoNDups:
        santiagoNDups.append(santiagoNum)
print("Sin duplicados:", santiagoNDups)
