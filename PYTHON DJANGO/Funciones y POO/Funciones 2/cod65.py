from collections import Counter as SantiagoCounter

def SantiagoPFrec(SantiagoText, SantiagoTop=5):
    SantiagoList = SantiagoText.lower().split()
    SantiagoCont = SantiagoCounter(SantiagoList)
    return SantiagoCont.most_common(SantiagoTop)

SantiagoTexto = "David David David Santiago Beltran Pedraza Pedraza"
print(SantiagoPFrec(SantiagoTexto))
