SantiagoB_Val = [121, 7, 47, 22, 5, 15, 44, 911]
SantiagoMin = 45
SantiagoFilter = list(filter(lambda x: x > SantiagoMin, SantiagoB_Val))

print(f"Valores mayores que {SantiagoMin} en la lista: {SantiagoFilter}")
