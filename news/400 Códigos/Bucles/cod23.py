SantiagoB_Nums = [44, 48, 5, 17, 85, 11]
SantiagoBuscar = 1
SantiagoEncontrado = False

for SantiagoNum in SantiagoB_Nums:
    if SantiagoNum == SantiagoBuscar:
        SantiagoEncontrado = True
        break

print(f"¿Se encontró el número {SantiagoBuscar}? - Respuesta: {SantiagoEncontrado}")
