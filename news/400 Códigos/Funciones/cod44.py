def SantiagoConvertirDolarAPeso(SantiagoDolares, SantiagoTasa):
    return SantiagoDolares * SantiagoTasa

def SantiagoMain():
    try:
        SantiagoD = float(input("Cantidad en dólares: "))
        SantiagoT = float(input("Tasa de cambio actual: "))
        print(f"Equivalente en pesos: {SantiagoConvertirDolarAPeso(SantiagoD, SantiagoT):,.2f}")
    except:
        print("Datos inválidos.")

SantiagoMain()
