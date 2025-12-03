#Imprime según el elemento escojido el número de veces que esta en la lista

santiagoList = [1, 2, 1, 3, 1, 4]
santiagoElement = santiagoList[0]
santiagoCont = 0
for santiagoN in santiagoList:
    if santiagoN == santiagoElement:
        santiagoCont += 1
print("El elemento ", santiagoElement, " esta ", santiagoCont, " veces en la lista")
