def SantiagoClasif(SantiagoList):
    SantiagoDict = {}
    for SantiagoP in SantiagoList:
        SantiagoLong = len(SantiagoP)
        if SantiagoLong not in SantiagoDict:
            SantiagoDict[SantiagoLong] = []
        SantiagoDict[SantiagoLong].append(SantiagoP)
    return SantiagoDict

SantiagoPalabras = ["Beltran", "Pedraza", "David", "Santiago"]
print(f"Contador: {SantiagoClasif(SantiagoPalabras)}")
