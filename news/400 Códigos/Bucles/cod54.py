import random
SantiagoB = 0
SantiagoInten = 0
while SantiagoB != 6:
    SantiagoB = random.randint(1, 6)
    SantiagoInten += 1
    print("Lanzamiento:", SantiagoB)
print(f"El dado con número 6 salió después de {SantiagoInten} intentos.")
