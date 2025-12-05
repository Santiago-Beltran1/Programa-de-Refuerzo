import pandas as SantiagoPd
import numpy as SantiagoNp

def SantiagoDataFrame(SantiagoFilas, SantiagoColumns):
    SantiagoDatos = SantiagoNp.random.randint(0, 100, (SantiagoFilas, SantiagoColumns))
    SantiagoColumnNames = [f"SantiagoCol{i}" for i in range(SantiagoColumns)]
    return SantiagoPd.DataFrame(SantiagoDatos, columns=SantiagoColumnNames)

print(SantiagoDataFrame(4, 3))
