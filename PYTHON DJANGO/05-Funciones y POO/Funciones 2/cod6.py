from collections import Counter

def SantiagoCont(SantiagoT):
    SantiagoP = SantiagoT.split()
    return Counter(SantiagoP)

print(f"El número de palabras que hay en el texto 'David Santiago Beltran Pedraza' son {SantiagoCont("David Santiago Beltran Pedraza")}")
