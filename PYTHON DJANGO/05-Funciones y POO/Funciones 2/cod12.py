from collections import Counter as SantiagoCounter

def SantiagoCont(SantiagoTexto):
    return SantiagoCounter(SantiagoTexto.replace(" ", ""))

SantiagoFrase = "David Santiago Beltran Pedraza"
print(f"El texto 'David Santiago Beltran Pedraza' tiene el siguiente número de por cada letra {SantiagoCont(SantiagoFrase)}")
