import numpy as np

def SantiagoAnaliz(SantiagoLista):
    SantiagoArr = np.array(SantiagoLista)
    return {
        "Suma": np.sum(SantiagoArr),
        "Media": np.mean(SantiagoArr),
        "Max": np.max(SantiagoArr),
        "Min": np.min(SantiagoArr)
    }

SantiagoDatos = [15, 142, 49, 80]
print(SantiagoAnaliz(SantiagoDatos))
