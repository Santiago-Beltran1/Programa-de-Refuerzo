print("Forma Tradicional: ")
SantiagoB_Cuadrado = [] 
for SantiagoX in range(11):
    SantiagoB_Cuadrado.append(SantiagoX**2)
print(SantiagoB_Cuadrado)

#Por comprensión de listas
print("Por comprensión de listas: ")
SantiagoB_Cuadrado = [SantiagoX**2 for SantiagoX in range(5)]
print(SantiagoB_Cuadrado)