def SantiagoAnalisis(SantiagoLista):
    SantiagoLista.sort()
    SantiagoN = len(SantiagoLista)
    SantiagoMediana = (SantiagoLista[SantiagoN//2] if SantiagoN % 2 != 0 else (SantiagoLista[SantiagoN//2 - 1] + SantiagoLista[SantiagoN//2]) / 2)
    return sum(SantiagoLista)/SantiagoN, SantiagoMediana, max(SantiagoLista)

def SantiagoMain():
    try:
        SantiagoDatos = [float(x) for x in input("Números separados por comas: ").split(",")]
        SantiagoMedia, SantiagoMediana, SantiagoMax = SantiagoAnalisis(SantiagoDatos)
        print(f"Media: {SantiagoMedia}, Mediana: {SantiagoMediana}, Máximo: {SantiagoMax}")
    except:
        print("Error en los datos.")

SantiagoMain()
