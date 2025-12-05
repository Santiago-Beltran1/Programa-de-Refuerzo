def SantiagoPerimetroRect(SantiagoBase, SantiagoAltura):
    return 2 * (SantiagoBase + SantiagoAltura)

def SantiagoMain():
    try:
        SantiagoB = float(input("Base: "))
        SantiagoA = float(input("Altura: "))
        print(f"Perímetro: {SantiagoPerimetroRect(SantiagoB, SantiagoA)}")
    except:
        print("Datos inválidos.")

SantiagoMain()
