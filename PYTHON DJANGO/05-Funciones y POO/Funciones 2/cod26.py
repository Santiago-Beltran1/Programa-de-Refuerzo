def SantiagoFilt(SantiagoList, SantiagoL):
    return [SantiagoP for SantiagoP in SantiagoList if SantiagoL in SantiagoP]

SantiagoListaPalabras = ["David", "Santiago", "Beltran", "Pedraza"]
print(f"Palabras de la lista que contienen la letra o: {SantiagoFilt(SantiagoListaPalabras, "o")}")
