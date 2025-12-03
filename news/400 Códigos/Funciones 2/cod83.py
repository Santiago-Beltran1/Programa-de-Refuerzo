def SantiagoAnali(SantiagoT):
    SantiagoOra = SantiagoT.count(".") + SantiagoT.count("!") + SantiagoT.count("?")
    SantiagoP = len(SantiagoT.split())
    print(f"Análisis del texto: {SantiagoP} palabras, {SantiagoOra} oraciones")

SantiagoAnali("Mi nombre es David Santiago Beltarn Pedraza")
