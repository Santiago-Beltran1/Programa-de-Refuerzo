import random

def SantiagoBFraseRandom():
    SantiagoSuj = ["Un gato", "Mi tío", "Un programador", "El robot SantiagoB"]
    SantiagoVerb = ["comió", "bailó", "rompió", "descubrió", "pintó"]
    SantiagoObj = ["una pizza", "el teclado", "una galaxia", "el sistema solar"]
    SantiagoLug = ["en el baño", "en Marte", "en un café", "en la oficina"]
    print(random.choice(SantiagoSuj), random.choice(SantiagoVerb), random.choice(SantiagoObj), random.choice(SantiagoLug))

SantiagoBFraseRandom()
