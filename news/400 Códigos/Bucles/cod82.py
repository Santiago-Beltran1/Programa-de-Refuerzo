SantiagoB = input("Ingrese un texto: ")
SantiagoP = SantiagoB.split()
for SantiagoP in SantiagoP:
    if SantiagoP[0].isupper():
        print(f"Las palabra con mayúscula que hay en el texto son: {SantiagoP}")
