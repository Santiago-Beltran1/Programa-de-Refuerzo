def SantiagoB(SantiagoBase, SantiagoAltura):
    santiagoPerimetro = 2 * (SantiagoBase + SantiagoAltura)
    return santiagoPerimetro

SantiagoR = SantiagoB(11, 25)
print(f"El perímetro del rectángulo es: {SantiagoR} metros")
